# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login_gift.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='login_gift.proto',
  package='',
  serialized_pb='\n\x10login_gift.proto\x1a\x0c\x63ommon.proto\"0\n\tLoginInfo\x12\x11\n\tlogin_day\x18\x01 \x02(\x05\x12\x10\n\x08is_new_p\x18\x02 \x02(\x05\"\x99\x01\n\x15InitLoginGiftResponse\x12\x1b\n\x13\x63umulative_received\x18\x01 \x03(\x05\x12\x1b\n\x13\x63ontinuous_received\x18\x02 \x03(\x05\x12\"\n\x0e\x63umulative_day\x18\x03 \x02(\x0b\x32\n.LoginInfo\x12\"\n\x0e\x63ontinuous_day\x18\x04 \x02(\x0b\x32\n.LoginInfo\"A\n\x13GetLoginGiftRequest\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x02(\x05\x12\x15\n\ractivity_type\x18\x02 \x02(\x05\"_\n\x14GetLoginGiftResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x11\n\tresult_no\x18\x02 \x01(\x05\x12$\n\x04gain\x18\x03 \x01(\x0b\x32\x16.GameResourcesResponse')




_LOGININFO = _descriptor.Descriptor(
  name='LoginInfo',
  full_name='LoginInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='login_day', full_name='LoginInfo.login_day', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_new_p', full_name='LoginInfo.is_new_p', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=34,
  serialized_end=82,
)


_INITLOGINGIFTRESPONSE = _descriptor.Descriptor(
  name='InitLoginGiftResponse',
  full_name='InitLoginGiftResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cumulative_received', full_name='InitLoginGiftResponse.cumulative_received', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='continuous_received', full_name='InitLoginGiftResponse.continuous_received', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cumulative_day', full_name='InitLoginGiftResponse.cumulative_day', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='continuous_day', full_name='InitLoginGiftResponse.continuous_day', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
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
  serialized_start=85,
  serialized_end=238,
)


_GETLOGINGIFTREQUEST = _descriptor.Descriptor(
  name='GetLoginGiftRequest',
  full_name='GetLoginGiftRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_id', full_name='GetLoginGiftRequest.activity_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity_type', full_name='GetLoginGiftRequest.activity_type', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  serialized_start=240,
  serialized_end=305,
)


_GETLOGINGIFTRESPONSE = _descriptor.Descriptor(
  name='GetLoginGiftResponse',
  full_name='GetLoginGiftResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GetLoginGiftResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_no', full_name='GetLoginGiftResponse.result_no', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gain', full_name='GetLoginGiftResponse.gain', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=307,
  serialized_end=402,
)

_INITLOGINGIFTRESPONSE.fields_by_name['cumulative_day'].message_type = _LOGININFO
_INITLOGINGIFTRESPONSE.fields_by_name['continuous_day'].message_type = _LOGININFO
_GETLOGINGIFTRESPONSE.fields_by_name['gain'].message_type = common_pb2._GAMERESOURCESRESPONSE
DESCRIPTOR.message_types_by_name['LoginInfo'] = _LOGININFO
DESCRIPTOR.message_types_by_name['InitLoginGiftResponse'] = _INITLOGINGIFTRESPONSE
DESCRIPTOR.message_types_by_name['GetLoginGiftRequest'] = _GETLOGINGIFTREQUEST
DESCRIPTOR.message_types_by_name['GetLoginGiftResponse'] = _GETLOGINGIFTRESPONSE

class LoginInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LOGININFO

  # @@protoc_insertion_point(class_scope:LoginInfo)

class InitLoginGiftResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _INITLOGINGIFTRESPONSE

  # @@protoc_insertion_point(class_scope:InitLoginGiftResponse)

class GetLoginGiftRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETLOGINGIFTREQUEST

  # @@protoc_insertion_point(class_scope:GetLoginGiftRequest)

class GetLoginGiftResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETLOGINGIFTRESPONSE

  # @@protoc_insertion_point(class_scope:GetLoginGiftResponse)


# @@protoc_insertion_point(module_scope)
