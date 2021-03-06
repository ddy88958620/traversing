# -*- coding:utf-8 -*-
"""
created by server on 14-8-22下午2:45.
"""

from robot import Robot
from app.proto_file import friend_pb2
from app.proto_file.common_pb2 import CommonResponse


class RobotFriend(Robot):
    def command_get_friend_list(self):
        request = friend_pb2.FriendCommon()
        self.send_message(request, 1106)

    def command_add_friend(self, target_id):
        request = friend_pb2.FriendCommon()
        request.target_ids.append(int(target_id))
        # self.send_message(request, 1101)
        self.send_message(request, 1100)

    def command_accept_friend(self, target_id):
        request = friend_pb2.FriendCommon()
        request.target_ids.append(int(target_id))
        self.send_message(request, 1101)

    def command_refuse_friend(self, target_id):
        request = friend_pb2.FriendCommon()
        request.target_ids.append(int(target_id))
        self.send_message(request, 1102)

    def command_find_friend(self, key):
        request = friend_pb2.FindFriendRequest()
        request.id_or_nickname = key
        self.send_message(request, 1107)

    def get_friend_list_1106(self, message):
        # get friend list
        response = friend_pb2.GetPlayerFriendsResponse()
        response.ParseFromString(message)
        # print 'get friends list:'
        print 'frinds:', len(response.friends)
        for _ in response.friends:
            print 'friend:', _
        print 'blacklist:', len(response.blacklist)
        for _ in response.blacklist:
            print 'blacklist:', _
        print 'applicant list:', len(response.applicant_list)
        for _ in response.applicant_list:
            print 'applicant list:', _

        self.on_command_finish()

    def get_add_friend_1100(self, message):
        response = CommonResponse()
        response.ParseFromString(message)
        str_format = 'add friend result:%s result_no:%s'
        print str_format % (response.result, response.result_no)
        self.on_command_finish()

    def get_refuse_friend_1102(self, message):
        response = CommonResponse()
        response.ParseFromString(message)
        str_format = 'refuse friend result:%s result_no:%s'
        print str_format % (response.result, response.result_no)
        self.on_command_finish()

    def get_find_friend_1107(self, message):
        response = friend_pb2.FindFriendResponse()
        response.ParseFromString(message)
        print 'find friend id:%s name:%s' % (response.id, response.nickname)
        self.on_command_finish()

    def get_accept_friend_1101(self, message):
        response = CommonResponse()
        response.ParseFromString(message)
        str_format = 'accept friend result:%s result_no:%s'
        print str_format % (response.result, response.result_no)
        self.on_command_finish()
