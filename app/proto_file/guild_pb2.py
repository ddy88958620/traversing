# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: guild.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='guild.proto',
  package='',
  serialized_pb='\n\x0bguild.proto\"I\n\x13GuildCommonResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x11\n\tresult_no\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"\x93\x01\n\tGuildInfo\x12\x0c\n\x04g_id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\x0c\x12\r\n\x05p_num\x18\x03 \x02(\x05\x12\r\n\x05level\x18\x04 \x02(\x05\x12\x0b\n\x03\x65xp\x18\x05 \x02(\x05\x12\x0c\n\x04\x66und\x18\x06 \x02(\x05\x12\x0c\n\x04\x63\x61ll\x18\x07 \x02(\x0c\x12\x0e\n\x06record\x18\x08 \x02(\x05\x12\x13\n\x0bmy_position\x18\t \x02(\x05\"]\n\x08RoleInfo\x12\x0c\n\x04p_id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\x0c\x12\r\n\x05level\x18\x03 \x02(\x05\x12\x11\n\tvip_level\x18\x04 \x02(\x05\x12\x13\n\x0b\x66ight_power\x18\x05 \x02(\x05\"q\n\tRoleInfo1\x12\x0c\n\x04p_id\x18\x01 \x02(\x05\x12\x0c\n\x04name\x18\x02 \x02(\x0c\x12\r\n\x05level\x18\x03 \x02(\x05\x12\x10\n\x08position\x18\x04 \x02(\x05\x12\x18\n\x10\x61ll_contribution\x18\x05 \x02(\x05\x12\r\n\x05k_num\x18\x06 \x02(\x05\"v\n\tGuildRank\x12\x0c\n\x04g_id\x18\x01 \x02(\t\x12\x0c\n\x04rank\x18\x02 \x02(\x05\x12\x0c\n\x04name\x18\x03 \x02(\x0c\x12\r\n\x05level\x18\x04 \x02(\x05\x12\x11\n\tpresident\x18\x05 \x02(\x0c\x12\r\n\x05p_num\x18\x06 \x02(\x05\x12\x0e\n\x06record\x18\x07 \x02(\x05\"\"\n\x12\x43reateGuildRequest\x12\x0c\n\x04name\x18\x01 \x02(\x0c\" \n\x10JoinGuildRequest\x12\x0c\n\x04g_id\x18\x01 \x02(\t\"[\n\x11JoinGuildResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x11\n\tresult_no\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\x0c\x12\x12\n\nspare_time\x18\x04 \x03(\x05\"!\n\x11\x45\x64itorCallRequest\x12\x0c\n\x04\x63\x61ll\x18\x02 \x02(\x0c\"3\n\x10\x44\x65\x61lApplyRequest\x12\r\n\x05p_ids\x18\x01 \x03(\x05\x12\x10\n\x08res_type\x18\x02 \x02(\x05\"V\n\x11\x44\x65\x61lApplyResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x11\n\tresult_no\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\x0c\x12\r\n\x05p_ids\x18\x04 \x03(\x05\"&\n\x16\x43hangePresidentRequest\x12\x0c\n\x04p_id\x18\x01 \x02(\x05\"\x1c\n\x0bKickRequest\x12\r\n\x05p_ids\x18\x01 \x03(\x05\"U\n\x11PromotionResponse\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x11\n\tresult_no\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\x0c\x12\x0c\n\x04p_id\x18\x04 \x01(\x05\" \n\x0eWorshipRequest\x12\x0e\n\x06w_type\x18\x01 \x02(\x05\"Q\n\x0eGuildInfoProto\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x1e\n\nguild_info\x18\x02 \x01(\x0b\x32\n.GuildInfo\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"O\n\x0e\x41pplyListProto\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x1c\n\trole_info\x18\x02 \x03(\x0b\x32\t.RoleInfo\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"T\n\x12GuildRoleListProto\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x1d\n\trole_info\x18\x02 \x03(\x0b\x32\n.RoleInfo1\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"Q\n\x0eGuildRankProto\x12\x0e\n\x06result\x18\x01 \x02(\x08\x12\x1e\n\nguild_rank\x18\x02 \x03(\x0b\x32\n.GuildRank\x12\x0f\n\x07message\x18\x03 \x01(\x0c')




_GUILDCOMMONRESPONSE = _descriptor.Descriptor(
  name='GuildCommonResponse',
  full_name='GuildCommonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GuildCommonResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_no', full_name='GuildCommonResponse.result_no', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='GuildCommonResponse.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=15,
  serialized_end=88,
)


_GUILDINFO = _descriptor.Descriptor(
  name='GuildInfo',
  full_name='GuildInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='g_id', full_name='GuildInfo.g_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='GuildInfo.name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p_num', full_name='GuildInfo.p_num', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='GuildInfo.level', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='GuildInfo.exp', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fund', full_name='GuildInfo.fund', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='call', full_name='GuildInfo.call', index=6,
      number=7, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record', full_name='GuildInfo.record', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='my_position', full_name='GuildInfo.my_position', index=8,
      number=9, type=5, cpp_type=1, label=2,
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
  serialized_start=91,
  serialized_end=238,
)


_ROLEINFO = _descriptor.Descriptor(
  name='RoleInfo',
  full_name='RoleInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_id', full_name='RoleInfo.p_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='RoleInfo.name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='RoleInfo.level', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='RoleInfo.vip_level', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fight_power', full_name='RoleInfo.fight_power', index=4,
      number=5, type=5, cpp_type=1, label=2,
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
  serialized_end=333,
)


_ROLEINFO1 = _descriptor.Descriptor(
  name='RoleInfo1',
  full_name='RoleInfo1',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_id', full_name='RoleInfo1.p_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='RoleInfo1.name', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='RoleInfo1.level', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='RoleInfo1.position', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='all_contribution', full_name='RoleInfo1.all_contribution', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='k_num', full_name='RoleInfo1.k_num', index=5,
      number=6, type=5, cpp_type=1, label=2,
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
  serialized_start=335,
  serialized_end=448,
)


_GUILDRANK = _descriptor.Descriptor(
  name='GuildRank',
  full_name='GuildRank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='g_id', full_name='GuildRank.g_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='GuildRank.rank', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='GuildRank.name', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='GuildRank.level', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='president', full_name='GuildRank.president', index=4,
      number=5, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p_num', full_name='GuildRank.p_num', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='record', full_name='GuildRank.record', index=6,
      number=7, type=5, cpp_type=1, label=2,
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
  serialized_start=450,
  serialized_end=568,
)


_CREATEGUILDREQUEST = _descriptor.Descriptor(
  name='CreateGuildRequest',
  full_name='CreateGuildRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='CreateGuildRequest.name', index=0,
      number=1, type=12, cpp_type=9, label=2,
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
  serialized_start=570,
  serialized_end=604,
)


_JOINGUILDREQUEST = _descriptor.Descriptor(
  name='JoinGuildRequest',
  full_name='JoinGuildRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='g_id', full_name='JoinGuildRequest.g_id', index=0,
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
  serialized_start=606,
  serialized_end=638,
)


_JOINGUILDRESPONSE = _descriptor.Descriptor(
  name='JoinGuildResponse',
  full_name='JoinGuildResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='JoinGuildResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_no', full_name='JoinGuildResponse.result_no', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='JoinGuildResponse.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spare_time', full_name='JoinGuildResponse.spare_time', index=3,
      number=4, type=5, cpp_type=1, label=3,
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
  serialized_start=640,
  serialized_end=731,
)


_EDITORCALLREQUEST = _descriptor.Descriptor(
  name='EditorCallRequest',
  full_name='EditorCallRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='call', full_name='EditorCallRequest.call', index=0,
      number=2, type=12, cpp_type=9, label=2,
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
  serialized_start=733,
  serialized_end=766,
)


_DEALAPPLYREQUEST = _descriptor.Descriptor(
  name='DealApplyRequest',
  full_name='DealApplyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_ids', full_name='DealApplyRequest.p_ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='res_type', full_name='DealApplyRequest.res_type', index=1,
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
  serialized_start=768,
  serialized_end=819,
)


_DEALAPPLYRESPONSE = _descriptor.Descriptor(
  name='DealApplyResponse',
  full_name='DealApplyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='DealApplyResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_no', full_name='DealApplyResponse.result_no', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='DealApplyResponse.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p_ids', full_name='DealApplyResponse.p_ids', index=3,
      number=4, type=5, cpp_type=1, label=3,
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
  serialized_start=821,
  serialized_end=907,
)


_CHANGEPRESIDENTREQUEST = _descriptor.Descriptor(
  name='ChangePresidentRequest',
  full_name='ChangePresidentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_id', full_name='ChangePresidentRequest.p_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=909,
  serialized_end=947,
)


_KICKREQUEST = _descriptor.Descriptor(
  name='KickRequest',
  full_name='KickRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='p_ids', full_name='KickRequest.p_ids', index=0,
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
  serialized_start=949,
  serialized_end=977,
)


_PROMOTIONRESPONSE = _descriptor.Descriptor(
  name='PromotionResponse',
  full_name='PromotionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='PromotionResponse.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_no', full_name='PromotionResponse.result_no', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='PromotionResponse.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='p_id', full_name='PromotionResponse.p_id', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=979,
  serialized_end=1064,
)


_WORSHIPREQUEST = _descriptor.Descriptor(
  name='WorshipRequest',
  full_name='WorshipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='w_type', full_name='WorshipRequest.w_type', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  serialized_start=1066,
  serialized_end=1098,
)


_GUILDINFOPROTO = _descriptor.Descriptor(
  name='GuildInfoProto',
  full_name='GuildInfoProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GuildInfoProto.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_info', full_name='GuildInfoProto.guild_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='GuildInfoProto.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=1100,
  serialized_end=1181,
)


_APPLYLISTPROTO = _descriptor.Descriptor(
  name='ApplyListProto',
  full_name='ApplyListProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='ApplyListProto.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_info', full_name='ApplyListProto.role_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='ApplyListProto.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=1183,
  serialized_end=1262,
)


_GUILDROLELISTPROTO = _descriptor.Descriptor(
  name='GuildRoleListProto',
  full_name='GuildRoleListProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GuildRoleListProto.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='role_info', full_name='GuildRoleListProto.role_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='GuildRoleListProto.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=1264,
  serialized_end=1348,
)


_GUILDRANKPROTO = _descriptor.Descriptor(
  name='GuildRankProto',
  full_name='GuildRankProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='GuildRankProto.result', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guild_rank', full_name='GuildRankProto.guild_rank', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='GuildRankProto.message', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=1350,
  serialized_end=1431,
)

_GUILDINFOPROTO.fields_by_name['guild_info'].message_type = _GUILDINFO
_APPLYLISTPROTO.fields_by_name['role_info'].message_type = _ROLEINFO
_GUILDROLELISTPROTO.fields_by_name['role_info'].message_type = _ROLEINFO1
_GUILDRANKPROTO.fields_by_name['guild_rank'].message_type = _GUILDRANK
DESCRIPTOR.message_types_by_name['GuildCommonResponse'] = _GUILDCOMMONRESPONSE
DESCRIPTOR.message_types_by_name['GuildInfo'] = _GUILDINFO
DESCRIPTOR.message_types_by_name['RoleInfo'] = _ROLEINFO
DESCRIPTOR.message_types_by_name['RoleInfo1'] = _ROLEINFO1
DESCRIPTOR.message_types_by_name['GuildRank'] = _GUILDRANK
DESCRIPTOR.message_types_by_name['CreateGuildRequest'] = _CREATEGUILDREQUEST
DESCRIPTOR.message_types_by_name['JoinGuildRequest'] = _JOINGUILDREQUEST
DESCRIPTOR.message_types_by_name['JoinGuildResponse'] = _JOINGUILDRESPONSE
DESCRIPTOR.message_types_by_name['EditorCallRequest'] = _EDITORCALLREQUEST
DESCRIPTOR.message_types_by_name['DealApplyRequest'] = _DEALAPPLYREQUEST
DESCRIPTOR.message_types_by_name['DealApplyResponse'] = _DEALAPPLYRESPONSE
DESCRIPTOR.message_types_by_name['ChangePresidentRequest'] = _CHANGEPRESIDENTREQUEST
DESCRIPTOR.message_types_by_name['KickRequest'] = _KICKREQUEST
DESCRIPTOR.message_types_by_name['PromotionResponse'] = _PROMOTIONRESPONSE
DESCRIPTOR.message_types_by_name['WorshipRequest'] = _WORSHIPREQUEST
DESCRIPTOR.message_types_by_name['GuildInfoProto'] = _GUILDINFOPROTO
DESCRIPTOR.message_types_by_name['ApplyListProto'] = _APPLYLISTPROTO
DESCRIPTOR.message_types_by_name['GuildRoleListProto'] = _GUILDROLELISTPROTO
DESCRIPTOR.message_types_by_name['GuildRankProto'] = _GUILDRANKPROTO

class GuildCommonResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUILDCOMMONRESPONSE

  # @@protoc_insertion_point(class_scope:GuildCommonResponse)

class GuildInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUILDINFO

  # @@protoc_insertion_point(class_scope:GuildInfo)

class RoleInfo(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLEINFO

  # @@protoc_insertion_point(class_scope:RoleInfo)

class RoleInfo1(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROLEINFO1

  # @@protoc_insertion_point(class_scope:RoleInfo1)

class GuildRank(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUILDRANK

  # @@protoc_insertion_point(class_scope:GuildRank)

class CreateGuildRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CREATEGUILDREQUEST

  # @@protoc_insertion_point(class_scope:CreateGuildRequest)

class JoinGuildRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JOINGUILDREQUEST

  # @@protoc_insertion_point(class_scope:JoinGuildRequest)

class JoinGuildResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _JOINGUILDRESPONSE

  # @@protoc_insertion_point(class_scope:JoinGuildResponse)

class EditorCallRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EDITORCALLREQUEST

  # @@protoc_insertion_point(class_scope:EditorCallRequest)

class DealApplyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEALAPPLYREQUEST

  # @@protoc_insertion_point(class_scope:DealApplyRequest)

class DealApplyResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DEALAPPLYRESPONSE

  # @@protoc_insertion_point(class_scope:DealApplyResponse)

class ChangePresidentRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHANGEPRESIDENTREQUEST

  # @@protoc_insertion_point(class_scope:ChangePresidentRequest)

class KickRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KICKREQUEST

  # @@protoc_insertion_point(class_scope:KickRequest)

class PromotionResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PROMOTIONRESPONSE

  # @@protoc_insertion_point(class_scope:PromotionResponse)

class WorshipRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _WORSHIPREQUEST

  # @@protoc_insertion_point(class_scope:WorshipRequest)

class GuildInfoProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUILDINFOPROTO

  # @@protoc_insertion_point(class_scope:GuildInfoProto)

class ApplyListProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _APPLYLISTPROTO

  # @@protoc_insertion_point(class_scope:ApplyListProto)

class GuildRoleListProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUILDROLELISTPROTO

  # @@protoc_insertion_point(class_scope:GuildRoleListProto)

class GuildRankProto(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GUILDRANKPROTO

  # @@protoc_insertion_point(class_scope:GuildRankProto)


# @@protoc_insertion_point(module_scope)
