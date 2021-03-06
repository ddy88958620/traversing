# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: friend.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='friend.proto',
  package='',
  serialized_pb='\n\x0c\x66riend.proto\x1a\x0c\x63ommon.proto\"\"\n\x0c\x46riendCommon\x12\x12\n\ntarget_ids\x18\x01 \x03(\x05\"#\n\x11\x41\x64\x64\x46riendResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\"+\n\x11\x46indFriendRequest\x12\x16\n\x0eid_or_nickname\x18\x01 \x01(\x0c\"\xa2\x01\n\x12\x46indFriendResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x0f\n\x07hero_no\x18\x03 \x01(\x05\x12\x0c\n\x04gift\x18\x04 \x01(\x05\x12\r\n\x05power\x18\x05 \x01(\x02\x12\n\n\x02hp\x18\x06 \x01(\x02\x12\x0b\n\x03\x61tk\x18\x07 \x01(\x02\x12\x14\n\x0cphysical_def\x18\x08 \x01(\x02\x12\x11\n\tmagic_def\x18\t \x01(\x02\"\x19\n\x17GetPlayerFriendsRequest\"\x9d\x01\n\rCharacterInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\x0f\n\x07hero_no\x18\x03 \x01(\x05\x12\x0c\n\x04gift\x18\x04 \x01(\x05\x12\r\n\x05power\x18\x05 \x01(\x02\x12\n\n\x02hp\x18\x06 \x01(\x02\x12\x0b\n\x03\x61tk\x18\x07 \x01(\x02\x12\x14\n\x0cphysical_def\x18\x08 \x01(\x02\x12\x11\n\tmagic_def\x18\t \x01(\x02\"\xae\x01\n\x18GetPlayerFriendsResponse\x12\x14\n\x0copen_receive\x18\x01 \x01(\x05\x12\x10\n\x08page_num\x18\x02 \x01(\x05\x12\x1f\n\x07\x66riends\x18\x03 \x03(\x0b\x32\x0e.CharacterInfo\x12!\n\tblacklist\x18\x04 \x03(\x0b\x32\x0e.CharacterInfo\x12&\n\x0e\x61pplicant_list\x18\x05 \x03(\x0b\x32\x0e.CharacterInfo\"?\n\x18\x46riendPrivateChatRequest\x12\x12\n\ntarget_uid\x18\x01 \x01(\x05\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t')




_FRIENDCOMMON = _descriptor.Descriptor(
  name='FriendCommon',
  full_name='FriendCommon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_ids', full_name='FriendCommon.target_ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=30,
  serialized_end=64,
)


_ADDFRIENDRESPONSE = _descriptor.Descriptor(
  name='AddFriendResponse',
  full_name='AddFriendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='AddFriendResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=66,
  serialized_end=101,
)


_FINDFRIENDREQUEST = _descriptor.Descriptor(
  name='FindFriendRequest',
  full_name='FindFriendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id_or_nickname', full_name='FindFriendRequest.id_or_nickname', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=103,
  serialized_end=146,
)


_FINDFRIENDRESPONSE = _descriptor.Descriptor(
  name='FindFriendResponse',
  full_name='FindFriendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='FindFriendResponse.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='FindFriendResponse.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='FindFriendResponse.hero_no', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift', full_name='FindFriendResponse.gift', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='FindFriendResponse.power', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp', full_name='FindFriendResponse.hp', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='atk', full_name='FindFriendResponse.atk', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physical_def', full_name='FindFriendResponse.physical_def', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magic_def', full_name='FindFriendResponse.magic_def', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=149,
  serialized_end=311,
)


_GETPLAYERFRIENDSREQUEST = _descriptor.Descriptor(
  name='GetPlayerFriendsRequest',
  full_name='GetPlayerFriendsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=313,
  serialized_end=338,
)


_CHARACTERINFO = _descriptor.Descriptor(
  name='CharacterInfo',
  full_name='CharacterInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CharacterInfo.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='CharacterInfo.nickname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_no', full_name='CharacterInfo.hero_no', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gift', full_name='CharacterInfo.gift', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='CharacterInfo.power', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hp', full_name='CharacterInfo.hp', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='atk', full_name='CharacterInfo.atk', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physical_def', full_name='CharacterInfo.physical_def', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magic_def', full_name='CharacterInfo.magic_def', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=341,
  serialized_end=498,
)


_GETPLAYERFRIENDSRESPONSE = _descriptor.Descriptor(
  name='GetPlayerFriendsResponse',
  full_name='GetPlayerFriendsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='open_receive', full_name='GetPlayerFriendsResponse.open_receive', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_num', full_name='GetPlayerFriendsResponse.page_num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='friends', full_name='GetPlayerFriendsResponse.friends', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blacklist', full_name='GetPlayerFriendsResponse.blacklist', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applicant_list', full_name='GetPlayerFriendsResponse.applicant_list', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=501,
  serialized_end=675,
)


_FRIENDPRIVATECHATREQUEST = _descriptor.Descriptor(
  name='FriendPrivateChatRequest',
  full_name='FriendPrivateChatRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_uid', full_name='FriendPrivateChatRequest.target_uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='FriendPrivateChatRequest.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=677,
  serialized_end=740,
)

_GETPLAYERFRIENDSRESPONSE.fields_by_name['friends'].message_type = _CHARACTERINFO
_GETPLAYERFRIENDSRESPONSE.fields_by_name['blacklist'].message_type = _CHARACTERINFO
_GETPLAYERFRIENDSRESPONSE.fields_by_name['applicant_list'].message_type = _CHARACTERINFO
DESCRIPTOR.message_types_by_name['FriendCommon'] = _FRIENDCOMMON
DESCRIPTOR.message_types_by_name['AddFriendResponse'] = _ADDFRIENDRESPONSE
DESCRIPTOR.message_types_by_name['FindFriendRequest'] = _FINDFRIENDREQUEST
DESCRIPTOR.message_types_by_name['FindFriendResponse'] = _FINDFRIENDRESPONSE
DESCRIPTOR.message_types_by_name['GetPlayerFriendsRequest'] = _GETPLAYERFRIENDSREQUEST
DESCRIPTOR.message_types_by_name['CharacterInfo'] = _CHARACTERINFO
DESCRIPTOR.message_types_by_name['GetPlayerFriendsResponse'] = _GETPLAYERFRIENDSRESPONSE
DESCRIPTOR.message_types_by_name['FriendPrivateChatRequest'] = _FRIENDPRIVATECHATREQUEST

class FriendCommon(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDCOMMON

  # @@protoc_insertion_point(class_scope:FriendCommon)

class AddFriendResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ADDFRIENDRESPONSE

  # @@protoc_insertion_point(class_scope:AddFriendResponse)

class FindFriendRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FINDFRIENDREQUEST

  # @@protoc_insertion_point(class_scope:FindFriendRequest)

class FindFriendResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FINDFRIENDRESPONSE

  # @@protoc_insertion_point(class_scope:FindFriendResponse)

class GetPlayerFriendsRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPLAYERFRIENDSREQUEST

  # @@protoc_insertion_point(class_scope:GetPlayerFriendsRequest)

class CharacterInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHARACTERINFO

  # @@protoc_insertion_point(class_scope:CharacterInfo)

class GetPlayerFriendsResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETPLAYERFRIENDSRESPONSE

  # @@protoc_insertion_point(class_scope:GetPlayerFriendsResponse)

class FriendPrivateChatRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FRIENDPRIVATECHATREQUEST

  # @@protoc_insertion_point(class_scope:FriendPrivateChatRequest)


# @@protoc_insertion_point(module_scope)
