# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: player.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='player.proto',
  package='',
  serialized_pb='\n\x0cplayer.proto\"z\n\tFinancePB\x12\x0c\n\x04\x63oin\x18\x01 \x01(\x05\x12\x0c\n\x04gold\x18\x02 \x01(\x05\x12\x11\n\thero_soul\x18\x03 \x01(\x05\x12\x14\n\x0cjunior_stone\x18\x04 \x01(\x05\x12\x14\n\x0cmiddle_stone\x18\x05 \x01(\x05\x12\x12\n\nhigh_stone\x18\x06 \x01(\x05')




_FINANCEPB = _descriptor.Descriptor(
  name='FinancePB',
  full_name='FinancePB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin', full_name='FinancePB.coin', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='FinancePB.gold', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_soul', full_name='FinancePB.hero_soul', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='junior_stone', full_name='FinancePB.junior_stone', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='middle_stone', full_name='FinancePB.middle_stone', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high_stone', full_name='FinancePB.high_stone', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=16,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['FinancePB'] = _FINANCEPB

class FinancePB(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _FINANCEPB

  # @@protoc_insertion_point(class_scope:FinancePB)


# @@protoc_insertion_point(module_scope)
