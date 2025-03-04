
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='cosmos_proto/cosmos.proto', package='cosmos_proto', syntax='proto3', serialized_options=b'Z%github.com/regen-network/cosmos-proto', create_key=_descriptor._internal_create_key, serialized_pb=b"\n\x19cosmos_proto/cosmos.proto\x12\x0ccosmos_proto\x1a google/protobuf/descriptor.proto:9\n\x0einterface_type\x12\x1f.google.protobuf.MessageOptions\x18\xc9\xd6\x05 \x01(\t:?\n\x14implements_interface\x12\x1f.google.protobuf.MessageOptions\x18\xca\xd6\x05 \x01(\t::\n\x11accepts_interface\x12\x1d.google.protobuf.FieldOptions\x18\xc9\xd6\x05 \x01(\tB'Z%github.com/regen-network/cosmos-protob\x06proto3", dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR])
INTERFACE_TYPE_FIELD_NUMBER = 93001
interface_type = _descriptor.FieldDescriptor(name='interface_type', full_name='cosmos_proto.interface_type', index=0, number=93001, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
IMPLEMENTS_INTERFACE_FIELD_NUMBER = 93002
implements_interface = _descriptor.FieldDescriptor(name='implements_interface', full_name='cosmos_proto.implements_interface', index=1, number=93002, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ACCEPTS_INTERFACE_FIELD_NUMBER = 93001
accepts_interface = _descriptor.FieldDescriptor(name='accepts_interface', full_name='cosmos_proto.accepts_interface', index=2, number=93001, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
DESCRIPTOR.extensions_by_name['interface_type'] = interface_type
DESCRIPTOR.extensions_by_name['implements_interface'] = implements_interface
DESCRIPTOR.extensions_by_name['accepts_interface'] = accepts_interface
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(interface_type)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(implements_interface)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(accepts_interface)
DESCRIPTOR._options = None
