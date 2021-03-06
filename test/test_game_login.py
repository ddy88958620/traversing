# -*- coding:utf-8 -*-
"""
created by server on 14-6-23上午11:59.
"""
#coding:utf8

import struct

from twisted.internet import reactor, protocol
from app.proto_file import item_pb2
from app.proto_file import account_pb2
from app.proto_file import equipment_pb2
from app.proto_file.player_request_pb2 import PlayerLoginRequest
from app.proto_file.player_response_pb2 import PlayerResponse
from app.proto_file import line_up_pb2
from app.proto_file import stage_pb2
from app.proto_file.account_pb2 import AccountResponse, AccountLoginRequest


def sendData(sendstr,commandId):
    '''定义协议头
    '''
    HEAD_0 = chr(0)
    HEAD_1 = chr(0)
    HEAD_2 = chr(0)
    HEAD_3 = chr(0)
    ProtoVersion = chr(0)
    ServerVersion = 0
    sendstr = sendstr
    print 'len:', len(sendstr)
    data = struct.pack('!sssss3I',HEAD_0,HEAD_1,HEAD_2,\
                       HEAD_3,ProtoVersion,ServerVersion,\
                       len(sendstr)+4,commandId)
    senddata = data+sendstr
    return senddata

def resolveRecvdata(data):
    '''解析数据，根据定义的协议头解析服务器返回的数据
    '''
    ud = struct.unpack('!sssss3I', data[:17])
    HEAD_0 = ord(ud[0])
    HEAD_1 = ord(ud[1])
    HEAD_2 = ord(ud[2])
    HEAD_3 = ord(ud[3])
    protoVersion = ord(ud[4])
    serverVersion = ud[5]
    lenght = ud[6]
    command = ud[7]
    message = data[17:17+lenght]
    print command, message

    return command, message

# a client protocol
times = 0
class EchoClient(protocol.Protocol):
    """Once connected, send a message, then print the result."""

    def dateSend(self, argument, command_id):
        self.transport.write(sendData(argument.SerializeToString(), command_id))

    def connectionMade(self):

        # 帐号登录

        argument = account_pb2.AccountLoginRequest()
        argument.key.key = '1e596c85f2234864c451219a7263b45d'

        # argument.user_name = 'ghh0001'
        # argument.password = '123457'
        self.dateSend(argument, 2)

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        command, message = resolveRecvdata(data)

        if command == 2:

            argument = AccountResponse()
            argument.ParseFromString(message)
            print argument

            argument = PlayerLoginRequest()
            argument.token = '1e596c85f2234864c451219a7263b45d'
            # self.dateSend(argument, 4)

        if command == 901:
            argument = stage_pb2.StageInfoResponse()
            argument.ParseFromString(message)

            for stage in argument.stage:
                print stage

            argument = stage_pb2.ChapterInfoRequest()
            argument.chapter_id = 0

            self.dateSend(argument, 902)

        if command == 902:
            argument = stage_pb2.ChapterInfoResponse()
            argument.ParseFromString(message)

            for award in argument.stage_award:
                print award


            argument = stage_pb2.StageStartRequest()
            argument.stage_id = 100100
            self.dateSend(argument, 903)


    def connectionLost(self, reason):
        print "connection lost"

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed - goodbye!"
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost - goodbye!"
        reactor.stop()


# this connects the protocol to a server runing on port 8000
def main():

    HOST = 'localhost'
    PORT = 11009

    f = EchoFactory()
    reactor.connectTCP(HOST, PORT, f)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()