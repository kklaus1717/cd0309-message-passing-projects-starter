# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: person.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'person.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cperson.proto\"\x94\x02\n\x0cOrderMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ncreated_by\x18\x02 \x01(\t\x12$\n\x06status\x18\x03 \x01(\x0e\x32\x14.OrderMessage.Status\x12\x12\n\ncreated_at\x18\x04 \x01(\t\x12*\n\tequipment\x18\x05 \x03(\x0e\x32\x17.OrderMessage.Equipment\"?\n\x06Status\x12\n\n\x06QUEUED\x10\x00\x12\x0e\n\nPROCESSING\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x12\n\n\x06\x46\x41ILED\x10\x03\"=\n\tEquipment\x12\x0c\n\x08KEYBOARD\x10\x00\x12\t\n\x05MOUSE\x10\x01\x12\n\n\x06WEBCAM\x10\x02\x12\x0b\n\x07MONITOR\x10\x03\"\x07\n\x05\x45mpty\"1\n\x10OrderMessageList\x12\x1d\n\x06orders\x18\x01 \x03(\x0b\x32\r.OrderMessage2X\n\x0cOrderService\x12&\n\x06\x43reate\x12\r.OrderMessage\x1a\r.OrderMessage\x12 \n\x03Get\x12\x06.Empty\x1a\x11.OrderMessageListb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'person_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ORDERMESSAGE']._serialized_start=17
  _globals['_ORDERMESSAGE']._serialized_end=293
  _globals['_ORDERMESSAGE_STATUS']._serialized_start=167
  _globals['_ORDERMESSAGE_STATUS']._serialized_end=230
  _globals['_ORDERMESSAGE_EQUIPMENT']._serialized_start=232
  _globals['_ORDERMESSAGE_EQUIPMENT']._serialized_end=293
  _globals['_EMPTY']._serialized_start=295
  _globals['_EMPTY']._serialized_end=302
  _globals['_ORDERMESSAGELIST']._serialized_start=304
  _globals['_ORDERMESSAGELIST']._serialized_end=353
  _globals['_ORDERSERVICE']._serialized_start=355
  _globals['_ORDERSERVICE']._serialized_end=443
# @@protoc_insertion_point(module_scope)
