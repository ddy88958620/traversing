# -*- coding:utf-8 -*-
"""
created by server on 14-6-16下午4:20.
"""
import os
import sys
import lupa
import codecs
import xlrd
import json
import cPickle
import MySQLdb
import sqlite3
import traceback
from lupa import LuaRuntime
from collections import OrderedDict

PROP_TABLE = ['base_config']


conn = MySQLdb.connect(host="127.0.0.1", user="root", passwd="123456", port=3306, db="traversing_master", charset="utf8")

_escape_string = MySQLdb._mysql.escape_string

def _escape(arg):
    """ format sql with args, take from dbapi src.
    """
    if type(arg) == str:
        arg = "'%s'" % _escape_string(arg)
    elif type(arg) == unicode:
        arg = "'%s'" % _escape_string(arg).encode('utf8')
    elif arg is None:
        arg = 'null'
    else:
        arg = str(arg)
    return arg


def update_configs(config_key, config_value):
    sql = "update configs set config_value=%s where config_key='%s';" % (_escape(config_value), config_key)
    print sql
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return


def insert_configs(config_key, config_value):
    sql = "insert into configs values ('%s', %s);" % (config_key, _escape(config_value))
    print sql
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return


def select_configs(config_key):
    sql = "SELECT * from configs where config_key = '%s';" % (config_key)
    print sql
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result


def save_to_file(json_data, path, name, prop_table):
    lua = LuaRuntime()

    lua.require("serialize_json")
    if name in prop_table:
        func = lua.eval('''function(json_data, path, name) save_to_file_prop(json_data, path, name); end''')
        func(json_data, path, name)
    else:
        func = lua.eval('''function(json_data, path, name) save_to_file(json_data, path, name); end''')
        func(json_data, path, name)


#if __name__ == "__main__":
#    save_to_file("[{'id':1}]", "b.lua", "b")


def ExcelToJson(ExcelFileName, SheetName, cur=None):
    print SheetName
    data = xlrd.open_workbook(ExcelFileName)
    table = data.sheet_by_name(SheetName)
    objName = ExcelFileName[:len(ExcelFileName) - 5]
    luaFileName = './lua/' + SheetName + ".lua"
    jsonFileName = './json/' + SheetName + ".json"

    if SheetName not in PROP_TABLE:
        table2jsn(table, jsonFileName, luaFileName, SheetName, cur)
    else:
        table2jsn_prop(table, jsonFileName, luaFileName, SheetName)


def FloatToString(aFloat):
    if type(aFloat) != float:
        return ""
    strTemp = str(aFloat)
    strList = strTemp.split(".")
    if len(strList) == 1:
        return strTemp
    else:
        if strList[1] == "0":
            return strList[0]
        else:
            return strTemp


def format_by_type(format_type, value):
    format_type = str(format_type).lower()

    if format_type == 'int':
        return int(value)

    if format_type == 'float':
        return float(value)

    if format_type == 'dict':
        return eval(value)

    if format_type == 'list':
        return eval(value)

    if format_type == 'str':
        if type(value) is float:
            return str(value).split('.')[0]
        return value.encode("utf-8")

    if format_type == 'eval':
        c = compile(value, '', 'eval')
        return value.encode("utf-8")


def table2jsn(table, jsonFileName, luaFileName, objName, cur=None):
    """标准表格式，每行一条数据"""
    nrows = table.nrows
    ncols = table.ncols

    if cur:
        create_table_sql = "create table %s (id integer primary key, content text)" % objName
        cur.execute("drop table if exists %s" % objName)
        cur.execute(create_table_sql)

    obj_list = []
    for rownum in range(nrows):
        if rownum == 0 or rownum == 1 or rownum == 2:
            continue

        print 'row:', rownum,
        obj = OrderedDict()
        for c in range(ncols):
            print c,
            prop_name = table.cell_value(1, c).encode("utf-8")
            prop_name = prop_name.strip()

            if prop_name == '#' or not prop_name:
                continue

            obj[prop_name] = format_by_type(table.cell_value(2, c), table.cell_value(rownum, c))

        obj_list.append(obj)

        print ''
        insert_data_sql = ""
        if objName == "hero_exp" or objName == "equipment_strengthen_config" or objName == "guild_config" \
                or objName == "hero_exp_config" or objName == "player_exp_config":
            insert_data_sql = "insert into %s values(%d, '%s');" % (objName, obj.get('level'), json.dumps(obj))
        else:
            insert_data_sql = "insert into %s values(%d, '%s');" % (objName, obj.get('id'), json.dumps(obj))

        print "insert_data_sql:", insert_data_sql
        if cur:
            try:
                cur.execute(insert_data_sql)
            except Exception, e:
                raise e
    #print 'obj_list:', json.dumps(obj_list)
    # print 'abc', json.dumps(obj_list, ensure_ascii=False)


    save_to_file(json.dumps(obj_list, ensure_ascii=False), luaFileName, objName, PROP_TABLE)
    with open(jsonFileName, mode='wb') as f:
        json.dump(obj_list, f)

    #
    # print "Create ", path, " OK"
    return


def table2jsn_prop(table, jsonFileName, luaFileName, objName):
    """属性表格式，每行一个属性"""
    nrows = table.nrows

    obj = {}
    begin_cols = 0
    for col in range(table.ncols):
        if table.cell_value(1, col) == "#":
            begin_cols += 1
        else:
            break
    for rownum in range(nrows):
        if rownum == 0 or rownum == 1 or rownum == 2:
            continue
        #print rownum, "row num +++++++++++++++++++++++"
        prop_name = table.cell_value(rownum, 0 + begin_cols).encode("utf-8")
        prop_name = prop_name.strip()

        obj[prop_name] = format_by_type(table.cell_value(rownum, 1 + begin_cols),
                                        table.cell_value(rownum, 2 + begin_cols))
    save_to_file(json.dumps(obj, ensure_ascii=False), luaFileName, objName, PROP_TABLE)
    # save_to_file("[{'id':1}]", path)
    with open(jsonFileName, mode='wb') as f:
        json.dump(obj, f)
    #
    # print "Create ", path, " OK"
    return


def save_update_sql(root_path, config_key, config_value):
    with open('%s%s.sql' % (root_path, 'update_' + config_key), 'w') as f:
        sql = "update configs set config_value=%s where config_key='%s';" % (_escape(config_value), config_key)
        f.write(sql)
    with open('%s%s.sql' % (root_path, 'insert_' + config_key), 'w') as f:
        sql = "insert into configs values('%s',%s); " % (config_key, _escape(config_value))
        f.write(sql)


def save_insert_all_sqls(root_path, content):
    with open('%s%s.sql' % (root_path, 'insert_all'), 'w') as f:
        for row in content:
            f.write(row)


if __name__ == "__main__":
    root_path = "./excel/"
    conn = sqlite3.connect("./db/config.db")
    cur = conn.cursor()

    content = []
    py_dict = {}
    for file_name in os.listdir(root_path):
        if not file_name.endswith("xlsx"):
            continue
        file_path = root_path + file_name
        file_with_out_extension = os.path.splitext(file_name)[0]
        print file_path, file_with_out_extension
        try:
            ExcelToJson(file_path, file_with_out_extension)
            ExcelToJson(file_path, file_with_out_extension, cur)
        except Exception, e:
            print 'table format error! table name:', file_name
            print traceback.print_exc()
            print 'message:', e
            exit(0)
        with open('./json/%s.json' % (file_with_out_extension), 'r') as f:
            json_data = json.load(f)

        config_value = cPickle.dumps(json_data)
        config_key = file_with_out_extension
        py_dict[config_key] = json_data
        save_update_sql('./sql/', config_key, config_value)

        delete_sql = "delete from configs where config_key='%s';\n" % (config_key)
        insert_sql = "insert into configs values('%s',%s); \n" % (config_key, _escape(config_value))
        content.append(delete_sql)
        content.append(insert_sql)

    cPickle.dump(py_dict, open('../../shared/db_opear/configs_data/excel', 'w'))
    save_insert_all_sqls('./sql/', content)
    conn.commit()
    print 'excel make successful!!!!!'