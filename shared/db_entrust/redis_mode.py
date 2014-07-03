#-*- coding:utf-8 -*-
"""
created by server on 14-5-28下午4:41.
"""
from shared.db_entrust.redis_client import redis_manager
from shared.db_entrust.redis_object import RedisObject
from gfirefly.dbentrust import util
import time
import cPickle

MMODE_STATE_ORI = 0  #未变更
MMODE_STATE_NEW = 1  #创建
MMODE_STATE_UPDATE = 2  #更新
MMODE_STATE_DEL = 3  #删除

TIMEOUT = 1800


def _insert(args):
    record, pkname, mmname, cls = args
    pk = record[pkname]
    mm = cls(mmname + ':%s' % pk, pkname, data=record)
    mm.insert()
    return pk


class PKValueError(ValueError):
    """
    """

    def __init__(self, data):
        ValueError.__init__(self)
        self.data = data

    def __str__(self):
        return "new record has no 'PK': %s" % (self.data)


class MMode(RedisObject):
    """内存数据模型，最终对应到的是表中的一条记录
    """

    def __init__(self, name, pk, data={}):
        """
        """
        super(MMode, self).__init__(name, redis_manager)
        self._state = MMODE_STATE_ORI  #对象的状态 0未变更  1新建 2更新 3删除
        self._pk = pk
        self.data = data
        self._time = float('%.02f' % time.time())

    def update(self, key, values):
        n_time = time.time()
        data = self.get_multi(['data', '_state'])

        data['data'].update({key: values})
        if data.get('_state') == MMODE_STATE_NEW:
            props = {'data': data.get('data'), '_time': n_time}
        else:
            props = {'_state': MMODE_STATE_UPDATE, 'data': data.get('data'), '_time': n_time}
        return RedisObject.update_multi(self, props)

    def update_multi(self, mapping):
        n_time = time.time()
        data = self.get_multi(['data', '_state'])
        data['data'].update(mapping)
        if data.get('_state') == MMODE_STATE_NEW:
            props = {'data': data.get('data'), '_time': n_time}
        else:
            props = {'_state': MMODE_STATE_UPDATE, 'data': data.get('data'), '_time': n_time}
        return RedisObject.update_multi(self, props)

    def get(self, key):
        n_time = time.time()
        RedisObject.update(self, "_time", n_time)
        return RedisObject.get(self, key)

    def get_multi(self, keys):

        n_time = time.time()
        RedisObject.update(self, "_time", n_time)
        return RedisObject.get_multi(self, keys)

    def delete(self):
        '''删除对象
        '''
        return RedisObject.update(self, '_state', MMODE_STATE_DEL)

    def mdelete(self):
        """清理对象
        """
        self.syncDB()
        RedisObject.mdelete(self)

    def IsEffective(self):
        '''检测对象是否有效
        '''
        if self.get('_state') == MMODE_STATE_DEL:
            return False
        return True

    def syncDB(self):
        """同步到数据库
        """
        state = int(self.get('_state'))
        print 'state:', state, type(state)
        tablename = self._name.split(':')[0]
        if state == MMODE_STATE_ORI:
            return
        elif state == MMODE_STATE_NEW:
            props = self.get('data')
            props = self.dumps(props)
            pk = self.get('_pk')
            print 'sync db props:',props
            result = util.InsertIntoDB(tablename, props)
            print 'result:', result
        elif state == MMODE_STATE_UPDATE:
            props = self.get('data')
            pk = self.get('_pk')
            props = self.dumps(props)
            prere = {pk: props.get(pk)}
            util.UpdateWithDict(tablename, props, prere)
            result = True
        else:
            pk = self.get('_pk')
            props = self.get('data')
            props = self.dumps(props)
            prere = {pk: props.get(pk)}
            result = util.DeleteFromDB(tablename, prere)
        if result:
            print '1111111111111111111111111;ljf;ljsadl;fjksad;l'
            RedisObject.update(self, '_state', MMODE_STATE_ORI)

    def checkSync(self, timeout=TIMEOUT):
        """检测同步
        """
        ntime = time.time()
        ntime = float('%.02f' % ntime)
        objtime = RedisObject.get(self, '_time')
        objtime = float(objtime)
        print objtime, type(objtime)
        print ntime, type(ntime)
        if ntime - objtime >= timeout and timeout:
            self.mdelete()
        else:
            print 'sync lll'
            self.syncDB()


class MFKMode(RedisObject):
    """外键内存数据模型
    """

    def __init__(self, name, pklist=[]):
        RedisObject.__init__(self, name, redis_manager)
        self.pklist = pklist


class MAdmin(RedisObject):
    """MMode对象管理，同一个MAdmin管理同一类的MMode，对应的是数据库中的某一种表
    """

    def __init__(self, name, pk, timeout=TIMEOUT, **kw):
        super(MAdmin, self).__init__(name, redis_manager)
        self._pk = pk
        self._fk = kw.get('fk', '')

        self._incrkey = kw.get('incrkey', '')
        self._incrvalue = kw.get('incrvalue', 0)
        self._timeout = timeout

    def insert(self):
        """将MAdmin配置的信息写入memcached中保存。\n当在其他的进程中实例化相同的配置的MAdmin，可以使得数据同步。
        """
        if self._incrkey and not self.get("_incrvalue"):
            self._incrvalue = util.GetTableIncrValue(self._name)
        else:
            self._incrvalue = self.get("_incrvalue")

        RedisObject.insert(self)

    def load(self):
        '''读取数据到数据库中
        '''
        mmname = self._name
        recordlist = util.ReadDataFromDB(mmname)
        for record in recordlist:
            pk = record[self._pk]
            record = MMode.loads(record)
            mm = MMode(self._name + ':%s' % pk, self._pk, data=record)
            mm.insert()

    @property
    def madmininfo(self):
        """作为一个特性属性。可以获取这个madmin的相关信息
        """
        keys = self.__dict__.keys()
        info = self.get_multi(keys)
        return info

    def getAllPkByFk(self, fk):
        '''根据外键获取主键列表
        '''
        name = '%s_fk:%s' % (self._name, fk)
        print 'fk name',name
        fkmm = MFKMode(name)
        pklist = fkmm.pklist

        print 'pklist type', type(pklist)
        print pklist
        if pklist:
            print "pk+++++++++++++++++++",pklist
            return pklist
        props = {self._fk: fk}
        print 'props',props
        dbkeylist = util.getAllPkByFkInDB(self._name, self._pk, props)

        name = '%s_fk:%s' % (self._name, fk)
        fkmm = MFKMode(name, pklist=dbkeylist)
        fkmm.insert()
        return dbkeylist

    def getObj(self, pk):
        '''根据主键，可以获得mmode对象的实例.\n
        >>> m = madmin.getObj(1)
        '''
        mm = MMode(self._name + ':%s' % pk, self._pk)
        if not mm.IsEffective():
            return None
        print '11111'
        if mm.get('data'):
            return mm
        print '222222'
        props = {self._pk: pk}
        record = util.GetOneRecordInfo(self._name, props)
        if not record:
            return None
        record = mm.loads(record)
        mm = MMode(self._name + ':%s' % pk, self._pk, data=record)
        mm.insert()
        return mm

    def getObjData(self, pk):
        '''根据主键，可以获得mmode对象的实例的数据.\n
        >>> m = madmin.getObjData(1)
        '''
        mm = MMode(self._name + ':%s' % pk, self._pk)

        print 'MMode:', mm.__dict__

        if not mm.IsEffective():
            return None
        data = mm.get('data')
        if mm.get('data'):
            print "record+++++++++++++++++++++++",type(data)
            return data
        props = {self._pk: pk}
        record = util.GetOneRecordInfo(self._name, props)
        print "record+++++++++++++++++++++",record
        if not record:
            return None

        record = mm.loads(record)
        mm = MMode(self._name + ':%s' % pk, self._pk, data=record)
        mm.insert()
        return record


    def getObjList(self, pklist):
        '''根据主键列表获取mmode对象的列表.\n
        >>> m = madmin.getObjList([1,2,3,4,5])
        '''
        _pklist = []
        objlist = []

        for pk in pklist:
            mm = MMode(self._name + ':%s' % pk, self._pk)
            if not mm.IsEffective():
                continue
            if mm.get('data'):
                objlist.append(mm)
            else:
                print "_pklist",_pklist
                _pklist.append(pk)
        if _pklist:
            recordlist = util.GetRecordList(self._name, self._pk, _pklist)
            for record in recordlist:
                pk = record[self._pk]
                mm = MMode(self._name + ':%s' % pk, self._pk)
                print "record++++++++++++++++++++", record
                print "record++++++++++++++++++++", record["hero_no"]
                record = mm.loads(record)
                print "record+++++++++++++++++",record.get("hero_no")
                mm = MMode(self._name + ':%s' % pk, self._pk, data=record)
                mm.insert()
                objlist.append(mm)
        return objlist

    def deleteMode(self, pk):
        '''根据主键删除内存中的某条记录信息，\n这里只是修改内存中的记录状态_state为删除状态.\n
        >>> m = madmin.deleteMode(1)
        '''
        mm = self.getObj(pk)
        if mm:
            if self._fk:
                data = mm.get('data')
                if data:
                    fk = data.get(self._fk, 0)
                    name = '%s_fk:%s' % (self._name, fk)
                    fkmm = MFKMode(name)
                    pklist = fkmm.get('pklist')
                    if pklist and pk in pklist:
                        pklist.remove(pk)
                    fkmm.update('pklist', pklist)
            mm.delete()
        return True

    def checkAll(self):
        """同步内存中的数据到对应的数据表中。\n
        >>> m = madmin.checkAll()
        """
        key = '%s:' % self._name
        _pklist = util.getredisallkeys(key, redis_manager)
        for pk in _pklist:
            mm = MMode(self._name + ':%s' % pk, self._pk)
            if not mm.IsEffective():
                mm.mdelete()
                continue
            if not mm.get('data'):
                continue
            mm.checkSync(timeout=self._timeout)
        self.deleteAllFk()

    def deleteAllFk(self):
        """删除所有的外键
        """
        key = '%s_fk:' % self._name
        _fklist = util.getredisallkeys(key, redis_manager)
        for fk in _fklist:
            name = '%s_fk:%s' % (self._name, fk)
            fkmm = MFKMode(name)
            fkmm.mdelete()

    def new(self, data):
        """创建一个新的对象
        """
        incrkey = self._incrkey
        if incrkey:
            incrvalue = self.incr('_incrvalue', 1)
            data[incrkey] = incrvalue - 1
            pk = data.get(self._pk)
            if pk is None:
                raise PKValueError(data)
            mm = MMode(self._name + ':%s' % pk, self._pk, data=data)
            setattr(mm, incrkey, pk)
        else:
            pk = data.get(self._pk)
            mm = MMode(self._name + ':%s' % pk, self._pk, data=data)
        if self._fk:
            fk = data.get(self._fk, 0)
            name = '%s_fk:%s' % (self._name, fk)
            fkmm = MFKMode(name)
            pklist = fkmm.get('pklist')
            if pklist is None:
                pklist = self.getAllPkByFk(fk)
            pklist.append(pk)
            fkmm.update('pklist', pklist)
        setattr(mm, '_state', MMODE_STATE_NEW)
        mm.insert()
        return mm

