# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: github.com/iost-official/go-iost/core/contract/contract.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='github.com/iost-official/go-iost/core/contract/contract.proto',
  package='contract',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=github.com/iost-official/go-iost/core/contract/contract.proto\x12\x08\x63ontract\"A\n\x04Info\x12\x0c\n\x04lang\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12\x1a\n\x03\x61\x62i\x18\x03 \x03(\x0b\x32\r.contract.ABI\"d\n\x03\x41\x42I\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07payment\x18\x02 \x01(\x05\x12\x1d\n\x05limit\x18\x03 \x01(\x0b\x32\x0e.contract.Cost\x12\x11\n\tgas_price\x18\x04 \x01(\x03\x12\x0c\n\x04\x61rgs\x18\x05 \x03(\t\".\n\x04\x43ost\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x03\x12\x0b\n\x03net\x18\x02 \x01(\x03\x12\x0b\n\x03\x43PU\x18\x03 \x01(\x03\"B\n\x08\x43ontract\x12\n\n\x02ID\x18\x01 \x01(\t\x12\x1c\n\x04info\x18\x02 \x01(\x0b\x32\x0e.contract.Info\x12\x0c\n\x04\x63ode\x18\x03 \x01(\tb\x06proto3')
)




_INFO = _descriptor.Descriptor(
  name='Info',
  full_name='contract.Info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lang', full_name='contract.Info.lang', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='contract.Info.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abi', full_name='contract.Info.abi', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=140,
)


_ABI = _descriptor.Descriptor(
  name='ABI',
  full_name='contract.ABI',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='contract.ABI.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment', full_name='contract.ABI.payment', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='contract.ABI.limit', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gas_price', full_name='contract.ABI.gas_price', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='args', full_name='contract.ABI.args', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=142,
  serialized_end=242,
)


_COST = _descriptor.Descriptor(
  name='Cost',
  full_name='contract.Cost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='contract.Cost.data', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='net', full_name='contract.Cost.net', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='CPU', full_name='contract.Cost.CPU', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=290,
)


_CONTRACT = _descriptor.Descriptor(
  name='Contract',
  full_name='contract.Contract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='contract.Contract.ID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='info', full_name='contract.Contract.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='code', full_name='contract.Contract.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=292,
  serialized_end=358,
)

_INFO.fields_by_name['abi'].message_type = _ABI
_ABI.fields_by_name['limit'].message_type = _COST
_CONTRACT.fields_by_name['info'].message_type = _INFO
DESCRIPTOR.message_types_by_name['Info'] = _INFO
DESCRIPTOR.message_types_by_name['ABI'] = _ABI
DESCRIPTOR.message_types_by_name['Cost'] = _COST
DESCRIPTOR.message_types_by_name['Contract'] = _CONTRACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Info = _reflection.GeneratedProtocolMessageType('Info', (_message.Message,), dict(
  DESCRIPTOR = _INFO,
  __module__ = 'github.com.iost_official.go_iost.core.contract.contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.Info)
  ))
_sym_db.RegisterMessage(Info)

ABI = _reflection.GeneratedProtocolMessageType('ABI', (_message.Message,), dict(
  DESCRIPTOR = _ABI,
  __module__ = 'github.com.iost_official.go_iost.core.contract.contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.ABI)
  ))
_sym_db.RegisterMessage(ABI)

Cost = _reflection.GeneratedProtocolMessageType('Cost', (_message.Message,), dict(
  DESCRIPTOR = _COST,
  __module__ = 'github.com.iost_official.go_iost.core.contract.contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.Cost)
  ))
_sym_db.RegisterMessage(Cost)

Contract = _reflection.GeneratedProtocolMessageType('Contract', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACT,
  __module__ = 'github.com.iost_official.go_iost.core.contract.contract_pb2'
  # @@protoc_insertion_point(class_scope:contract.Contract)
  ))
_sym_db.RegisterMessage(Contract)


# @@protoc_insertion_point(module_scope)
