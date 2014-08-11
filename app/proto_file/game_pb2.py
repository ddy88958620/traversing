# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='',
  serialized_pb='\n\ngame.proto\x1a\x0c\x63ommon.proto\"!\n\x10GameLoginRequest\x12\r\n\x05token\x18\x01 \x02(\t\"\xde\x02\n\x11GameLoginResponse\x12\x1c\n\x03res\x18\x01 \x02(\x0b\x32\x0f.CommonResponse\x12\n\n\x02id\x18\x11 \x01(\x05\x12\x10\n\x08nickname\x18\x02 \x01(\t\x12\r\n\x05level\x18\x03 \x01(\x05\x12\x0b\n\x03\x65xp\x18\x04 \x01(\x05\x12\x0c\n\x04\x63oin\x18\x05 \x01(\x05\x12\x0c\n\x04gold\x18\x06 \x01(\x05\x12\x11\n\thero_soul\x18\x07 \x01(\x05\x12\x14\n\x0cjunior_stone\x18\x08 \x01(\x05\x12\x14\n\x0cmiddle_stone\x18\t \x01(\x05\x12\x12\n\nhigh_stone\x18\n \x01(\x05\x12\x11\n\tfine_hero\x18\x0b \x01(\x05\x12\x16\n\x0e\x65xcellent_hero\x18\x0c \x01(\x05\x12\x16\n\x0e\x66ine_equipment\x18\r \x01(\x05\x12\x1b\n\x13\x65xcellent_equipment\x18\x0e \x01(\x05\x12\x0f\n\x07stamina\x18\x0f \x01(\x05\x12\x11\n\tpvp_times\x18\x10 \x01(\x05')




_GAMELOGINREQUEST = _descriptor.Descriptor(
  name='GameLoginRequest',
  full_name='GameLoginRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='GameLoginRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=2,
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
  serialized_start=28,
  serialized_end=61,
)


_GAMELOGINRESPONSE = _descriptor.Descriptor(
  name='GameLoginResponse',
  full_name='GameLoginResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='res', full_name='GameLoginResponse.res', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='GameLoginResponse.id', index=1,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='GameLoginResponse.nickname', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='GameLoginResponse.level', index=3,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='GameLoginResponse.exp', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='coin', full_name='GameLoginResponse.coin', index=5,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='GameLoginResponse.gold', index=6,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_soul', full_name='GameLoginResponse.hero_soul', index=7,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='junior_stone', full_name='GameLoginResponse.junior_stone', index=8,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='middle_stone', full_name='GameLoginResponse.middle_stone', index=9,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high_stone', full_name='GameLoginResponse.high_stone', index=10,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_hero', full_name='GameLoginResponse.fine_hero', index=11,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_hero', full_name='GameLoginResponse.excellent_hero', index=12,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fine_equipment', full_name='GameLoginResponse.fine_equipment', index=13,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='excellent_equipment', full_name='GameLoginResponse.excellent_equipment', index=14,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina', full_name='GameLoginResponse.stamina', index=15,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pvp_times', full_name='GameLoginResponse.pvp_times', index=16,
      number=16, type=5, cpp_type=1, label=1,
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
  serialized_start=64,
  serialized_end=414,
)

_GAMELOGINRESPONSE.fields_by_name['res'].message_type = common_pb2._COMMONRESPONSE
DESCRIPTOR.message_types_by_name['GameLoginRequest'] = _GAMELOGINREQUEST
DESCRIPTOR.message_types_by_name['GameLoginResponse'] = _GAMELOGINRESPONSE

class GameLoginRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMELOGINREQUEST

  # @@protoc_insertion_point(class_scope:GameLoginRequest)

class GameLoginResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMELOGINRESPONSE

  # @@protoc_insertion_point(class_scope:GameLoginResponse)


# @@protoc_insertion_point(module_scope)
