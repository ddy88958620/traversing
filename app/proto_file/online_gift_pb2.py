# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: online_gift.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='online_gift.proto',
  package='',
  serialized_pb='\n\x11online_gift.proto\x1a\x0c\x63ommon.proto\" \n\rGetOnlineGift\x12\x0f\n\x07gift_id\x18\x01 \x03(\x05')




_GETONLINEGIFT = _descriptor.Descriptor(
  name='GetOnlineGift',
  full_name='GetOnlineGift',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='GetOnlineGift.gift_id', index=0,
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
  serialized_start=35,
  serialized_end=67,
)

DESCRIPTOR.message_types_by_name['GetOnlineGift'] = _GETONLINEGIFT

class GetOnlineGift(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETONLINEGIFT

  # @@protoc_insertion_point(class_scope:GetOnlineGift)


# @@protoc_insertion_point(module_scope)
