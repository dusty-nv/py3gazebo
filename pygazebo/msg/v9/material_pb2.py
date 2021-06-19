# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: material.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import color_pb2 as color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='material.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x0ematerial.proto\x12\x0bgazebo.msgs\x1a\x0b\x63olor.proto\"\xb0\x03\n\x08Material\x12,\n\x06script\x18\x01 \x01(\x0b\x32\x1c.gazebo.msgs.Material.Script\x12\x35\n\x0bshader_type\x18\x02 \x01(\x0e\x32 .gazebo.msgs.Material.ShaderType\x12\x12\n\nnormal_map\x18\x03 \x01(\t\x12#\n\x07\x61mbient\x18\x04 \x01(\x0b\x32\x12.gazebo.msgs.Color\x12#\n\x07\x64iffuse\x18\x05 \x01(\x0b\x32\x12.gazebo.msgs.Color\x12$\n\x08specular\x18\x06 \x01(\x0b\x32\x12.gazebo.msgs.Color\x12$\n\x08\x65missive\x18\x07 \x01(\x0b\x32\x12.gazebo.msgs.Color\x12\x10\n\x08lighting\x18\x08 \x01(\x08\x1a#\n\x06Script\x12\x0b\n\x03uri\x18\x01 \x03(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\"^\n\nShaderType\x12\n\n\x06VERTEX\x10\x01\x12\t\n\x05PIXEL\x10\x02\x12\x1b\n\x17NORMAL_MAP_OBJECT_SPACE\x10\x03\x12\x1c\n\x18NORMAL_MAP_TANGENT_SPACE\x10\x04')
  ,
  dependencies=[color__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MATERIAL_SHADERTYPE = _descriptor.EnumDescriptor(
  name='ShaderType',
  full_name='gazebo.msgs.Material.ShaderType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VERTEX', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIXEL', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL_MAP_OBJECT_SPACE', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NORMAL_MAP_TANGENT_SPACE', index=3, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=383,
  serialized_end=477,
)
_sym_db.RegisterEnumDescriptor(_MATERIAL_SHADERTYPE)


_MATERIAL_SCRIPT = _descriptor.Descriptor(
  name='Script',
  full_name='gazebo.msgs.Material.Script',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='gazebo.msgs.Material.Script.uri', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='gazebo.msgs.Material.Script.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=346,
  serialized_end=381,
)

_MATERIAL = _descriptor.Descriptor(
  name='Material',
  full_name='gazebo.msgs.Material',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='script', full_name='gazebo.msgs.Material.script', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shader_type', full_name='gazebo.msgs.Material.shader_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normal_map', full_name='gazebo.msgs.Material.normal_map', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ambient', full_name='gazebo.msgs.Material.ambient', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diffuse', full_name='gazebo.msgs.Material.diffuse', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='specular', full_name='gazebo.msgs.Material.specular', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='emissive', full_name='gazebo.msgs.Material.emissive', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lighting', full_name='gazebo.msgs.Material.lighting', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MATERIAL_SCRIPT, ],
  enum_types=[
    _MATERIAL_SHADERTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=477,
)

_MATERIAL_SCRIPT.containing_type = _MATERIAL
_MATERIAL.fields_by_name['script'].message_type = _MATERIAL_SCRIPT
_MATERIAL.fields_by_name['shader_type'].enum_type = _MATERIAL_SHADERTYPE
_MATERIAL.fields_by_name['ambient'].message_type = color__pb2._COLOR
_MATERIAL.fields_by_name['diffuse'].message_type = color__pb2._COLOR
_MATERIAL.fields_by_name['specular'].message_type = color__pb2._COLOR
_MATERIAL.fields_by_name['emissive'].message_type = color__pb2._COLOR
_MATERIAL_SHADERTYPE.containing_type = _MATERIAL
DESCRIPTOR.message_types_by_name['Material'] = _MATERIAL

Material = _reflection.GeneratedProtocolMessageType('Material', (_message.Message,), dict(

  Script = _reflection.GeneratedProtocolMessageType('Script', (_message.Message,), dict(
    DESCRIPTOR = _MATERIAL_SCRIPT,
    __module__ = 'material_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.Material.Script)
    ))
  ,
  DESCRIPTOR = _MATERIAL,
  __module__ = 'material_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.Material)
  ))
_sym_db.RegisterMessage(Material)
_sym_db.RegisterMessage(Material.Script)


# @@protoc_insertion_point(module_scope)
