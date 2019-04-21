# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: heightmapgeom.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import image_pb2 as image__pb2
import vector3d_pb2 as vector3d__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='heightmapgeom.proto',
  package='gazebo.msgs',
  syntax='proto2',
  serialized_pb=_b('\n\x13heightmapgeom.proto\x12\x0bgazebo.msgs\x1a\x0bimage.proto\x1a\x0evector3d.proto\"\xbe\x03\n\rHeightmapGeom\x12!\n\x05image\x18\x01 \x01(\x0b\x32\x12.gazebo.msgs.Image\x12#\n\x04size\x18\x02 \x02(\x0b\x32\x15.gazebo.msgs.Vector3d\x12%\n\x06origin\x18\x03 \x01(\x0b\x32\x15.gazebo.msgs.Vector3d\x12\x0f\n\x07heights\x18\x04 \x03(\x02\x12\r\n\x05width\x18\x05 \x01(\x05\x12\x0e\n\x06height\x18\x06 \x01(\x05\x12\x33\n\x07texture\x18\x07 \x03(\x0b\x32\".gazebo.msgs.HeightmapGeom.Texture\x12/\n\x05\x62lend\x18\x08 \x03(\x0b\x32 .gazebo.msgs.HeightmapGeom.Blend\x12\x1a\n\x12use_terrain_paging\x18\t \x01(\x08\x12\x10\n\x08\x66ilename\x18\n \x01(\t\x12\x10\n\x08sampling\x18\x0b \x01(\r\x1a\x38\n\x07Texture\x12\x0f\n\x07\x64iffuse\x18\x01 \x02(\t\x12\x0e\n\x06normal\x18\x02 \x02(\t\x12\x0c\n\x04size\x18\x03 \x02(\x01\x1a.\n\x05\x42lend\x12\x12\n\nmin_height\x18\x01 \x02(\x01\x12\x11\n\tfade_dist\x18\x02 \x02(\x01')
  ,
  dependencies=[image__pb2.DESCRIPTOR,vector3d__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HEIGHTMAPGEOM_TEXTURE = _descriptor.Descriptor(
  name='Texture',
  full_name='gazebo.msgs.HeightmapGeom.Texture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diffuse', full_name='gazebo.msgs.HeightmapGeom.Texture.diffuse', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normal', full_name='gazebo.msgs.HeightmapGeom.Texture.normal', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='gazebo.msgs.HeightmapGeom.Texture.size', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
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
  serialized_start=408,
  serialized_end=464,
)

_HEIGHTMAPGEOM_BLEND = _descriptor.Descriptor(
  name='Blend',
  full_name='gazebo.msgs.HeightmapGeom.Blend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min_height', full_name='gazebo.msgs.HeightmapGeom.Blend.min_height', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fade_dist', full_name='gazebo.msgs.HeightmapGeom.Blend.fade_dist', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
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
  serialized_start=466,
  serialized_end=512,
)

_HEIGHTMAPGEOM = _descriptor.Descriptor(
  name='HeightmapGeom',
  full_name='gazebo.msgs.HeightmapGeom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image', full_name='gazebo.msgs.HeightmapGeom.image', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='gazebo.msgs.HeightmapGeom.size', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin', full_name='gazebo.msgs.HeightmapGeom.origin', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heights', full_name='gazebo.msgs.HeightmapGeom.heights', index=3,
      number=4, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='gazebo.msgs.HeightmapGeom.width', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='gazebo.msgs.HeightmapGeom.height', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='texture', full_name='gazebo.msgs.HeightmapGeom.texture', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='blend', full_name='gazebo.msgs.HeightmapGeom.blend', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_terrain_paging', full_name='gazebo.msgs.HeightmapGeom.use_terrain_paging', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='gazebo.msgs.HeightmapGeom.filename', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sampling', full_name='gazebo.msgs.HeightmapGeom.sampling', index=10,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_HEIGHTMAPGEOM_TEXTURE, _HEIGHTMAPGEOM_BLEND, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=512,
)

_HEIGHTMAPGEOM_TEXTURE.containing_type = _HEIGHTMAPGEOM
_HEIGHTMAPGEOM_BLEND.containing_type = _HEIGHTMAPGEOM
_HEIGHTMAPGEOM.fields_by_name['image'].message_type = image__pb2._IMAGE
_HEIGHTMAPGEOM.fields_by_name['size'].message_type = vector3d__pb2._VECTOR3D
_HEIGHTMAPGEOM.fields_by_name['origin'].message_type = vector3d__pb2._VECTOR3D
_HEIGHTMAPGEOM.fields_by_name['texture'].message_type = _HEIGHTMAPGEOM_TEXTURE
_HEIGHTMAPGEOM.fields_by_name['blend'].message_type = _HEIGHTMAPGEOM_BLEND
DESCRIPTOR.message_types_by_name['HeightmapGeom'] = _HEIGHTMAPGEOM

HeightmapGeom = _reflection.GeneratedProtocolMessageType('HeightmapGeom', (_message.Message,), dict(

  Texture = _reflection.GeneratedProtocolMessageType('Texture', (_message.Message,), dict(
    DESCRIPTOR = _HEIGHTMAPGEOM_TEXTURE,
    __module__ = 'heightmapgeom_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.HeightmapGeom.Texture)
    ))
  ,

  Blend = _reflection.GeneratedProtocolMessageType('Blend', (_message.Message,), dict(
    DESCRIPTOR = _HEIGHTMAPGEOM_BLEND,
    __module__ = 'heightmapgeom_pb2'
    # @@protoc_insertion_point(class_scope:gazebo.msgs.HeightmapGeom.Blend)
    ))
  ,
  DESCRIPTOR = _HEIGHTMAPGEOM,
  __module__ = 'heightmapgeom_pb2'
  # @@protoc_insertion_point(class_scope:gazebo.msgs.HeightmapGeom)
  ))
_sym_db.RegisterMessage(HeightmapGeom)
_sym_db.RegisterMessage(HeightmapGeom.Texture)
_sym_db.RegisterMessage(HeightmapGeom.Blend)


# @@protoc_insertion_point(module_scope)