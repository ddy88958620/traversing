# coding:utf8
'''
Created on 2013-8-14

@author: lan (www.9miao.com)
'''
from gfirefly.server.globalobject import GlobalObject, remoteserviceHandle


@remoteserviceHandle('gate')
def push_object_remote(topicID, msg, sendList):
    GlobalObject().netfactory.pushObject(topicID, msg, sendList)


@remoteserviceHandle('gate')
def disconnect_remote(connection_id):
    GlobalObject().netfactory.loseConnection(connection_id)
    return True


@remoteserviceHandle('gate')
def change_dynamic_id_remote(old_id, new_id):
    GlobalObject().netfactory.change_id(old_id, new_id)
    return True
