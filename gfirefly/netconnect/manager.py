# coding:utf8
'''
Created on 2014-2-23
连接管理器
@author: lan (www.9miao.com)
'''
from gfirefly.server.globalobject import GlobalObject

from gfirefly.server.logobj import logger
from connection import Connection
from shared.utils.const import const
import collections
import gevent


class ConnectionManager:
    ''' 连接管理器
    @param _connections: dict {connID:conn Object}管理的所有连接
    '''

    def __init__(self):
        '''初始化
        @param _connections: dict {connID:conn Object}
        '''
        self._connections = {}
        self._queue_conns = collections.OrderedDict()
        self.loop_check()

    def getNowConnCnt(self):
        '''获取当前连接数量'''
        return len(self._connections.items())

    @property
    def queue_num(self):
        return len(self._queue_conns)

    @property
    def connect_ids(self):
        return self._connections.keys()

    def hasConnection(self, dynamic_id):
        """是否包含连接"""
        return dynamic_id in self._connections.keys()

    def addConnection(self, conn):
        '''加入一条连接
        @param _conn: Conn object
        '''

        _conn = Connection(conn)
        if self._connections.has_key(_conn.dynamic_id):
            raise Exception("系统记录冲突")

        # 连接数达到上限，将连接缓存到队列中
        if const.MAX_CONNECTION <= len(self._connections):
            self._queue_conns[_conn.dynamic_id] = _conn
            return

        self._connections[_conn.dynamic_id] = _conn

    def dropConnectionByID(self, connID):
        '''更加连接的id删除连接实例
        @param connID: int 连接的id
        '''
        if connID in self._connections:
            del self._connections[connID]
        if connID in self._queue_conns:
            del self._queue_conns[connID]

    def getConnectionByID(self, connID):
        """根据ID获取一条连接
        @param connID: int 连接的id
        """
        return self._connections.get(connID, None)

    def loseConnection(self, connID):
        """根据连接ID主动端口与客户端的连接
        """
        conn = self.getConnectionByID(connID)
        if conn:
            conn.loseConnection()

    def change_id(self, new_id, cur_id):
        print "self._connections", self._connections, cur_id, new_id
        if cur_id not in self._connections:
            return False

        connection = self._connections[cur_id]
        if new_id in self._connections:
            old_connection = self._connections[new_id]
            old_connection.loseConnection()
            old_connection.dynamic_id = 0

        del self._connections[cur_id]
        self._connections[new_id] = connection
        connection.dynamic_id = new_id
        return True

    def pop_queue(self):
        if len(self._queue_conns) <= 0:
            return
        tmp = self._queue_conns.popitem(False)
        self._connections[tmp[0]] = tmp[1]
        return tmp[1]

    def __write_data(self, connection_id, topic_id, msg):
        connection = self.getConnectionByID(connection_id)
        if not connection:
            connection = self._queue_conns.get(connection_id, None)

        if not connection:
            return

        try:
            connection.safeToWriteData(topic_id, msg)
        except Exception, e:
            e = "%s, %s:%s" % (e, topic_id, msg)
            logger.exception(e)
            self.dropConnectionByID(connection_id)
            dynamic_id = connection.transport.sessionno
            if dynamic_id != 0:
                remote_gate = GlobalObject().remote['gate']
                remote_gate.net_conn_lost_remote_noresult(dynamic_id)

    def pushObject(self, topicID, msg, sendList):
        """主动推送消息"""
        if isinstance(sendList, list):
            for target in sendList:
                self.__write_data(target, topicID, msg)
        else:
            self.__write_data(sendList, topicID, msg)

    def check_timeout(self):
        for k, v in self._connections.items():
            if v.time_out:
                v.loseConnection()

    def loop_check(self):
        loop = gevent.get_hub().loop
        t = loop.timer(0.0, const.TIME_OUT / 4)
        t.start(self.check_timeout)
