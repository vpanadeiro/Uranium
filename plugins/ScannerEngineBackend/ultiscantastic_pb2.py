# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ultiscantastic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ultiscantastic.proto',
  package='ScannerBuff',
  serialized_pb=_b('\n\x14ultiscantastic.proto\x12\x0bScannerBuff\"F\n\x15PointCloudWithNormals\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08vertices\x18\x02 \x01(\x0c\x12\x0f\n\x07normals\x18\x03 \x01(\x0c\"8\n\x18PointCloudWithoutNormals\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08vertices\x18\x02 \x01(\x0c\"1\n\x15PointCloudPointNormal\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"2\n\x0eProgressUpdate\x12\x10\n\x08objectId\x18\x01 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x05\"F\n\x04Mesh\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08vertices\x18\x02 \x01(\x0c\x12\x0f\n\x07normals\x18\x03 \x01(\x0c\x12\x0f\n\x07indices\x18\x04 \x01(\x0c\"y\n\x10StartCalibration\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.ScannerBuff.StartCalibration.CalibrationType\"(\n\x0f\x43\x61librationType\x12\n\n\x06\x43ORNER\x10\x00\x12\t\n\x05\x42OARD\x10\x01\"[\n\tStartScan\x12-\n\x04type\x18\x01 \x01(\x0e\x32\x1f.ScannerBuff.StartScan.ScanType\"\x1f\n\x08ScanType\x12\x08\n\x04GREY\x10\x00\x12\t\n\x05PHASE\x10\x01\"\x80\x01\n\x05Image\x12*\n\x04type\x18\x01 \x01(\x0e\x32\x1c.ScannerBuff.Image.ImageType\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"\x1e\n\tImageType\x12\x08\n\x04MONO\x10\x00\x12\x07\n\x03RGB\x10\x01\"\xba\x01\n\x12setCalibrationStep\x12=\n\x04step\x18\x01 \x01(\x0e\x32/.ScannerBuff.setCalibrationStep.CalibrationStep\"e\n\x0f\x43\x61librationStep\x12\t\n\x05\x42OARD\x10\x00\x12\x13\n\x0fPROJECTOR_FOCUS\x10\x01\x12\x10\n\x0c\x43\x41MERA_FOCUS\x10\x02\x12\x13\n\x0f\x43\x41MERA_EXPOSURE\x10\x03\x12\x0b\n\x07\x43OMPUTE\x10\x04\"\xa5\x01\n\x12\x43\x61librationProblem\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.ScannerBuff.CalibrationProblem.Problem\"X\n\x07Problem\x12\x14\n\x10OBJECT_NOT_FOUND\x10\x00\x12\x16\n\x12PLATFORM_NOT_FOUND\x10\x01\x12\r\n\tNO_CAMERA\x10\x02\x12\x10\n\x0cNO_PROJECTOR\x10\x03\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STARTCALIBRATION_CALIBRATIONTYPE = _descriptor.EnumDescriptor(
  name='CalibrationType',
  full_name='ScannerBuff.StartCalibration.CalibrationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CORNER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOARD', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=423,
  serialized_end=463,
)
_sym_db.RegisterEnumDescriptor(_STARTCALIBRATION_CALIBRATIONTYPE)

_STARTSCAN_SCANTYPE = _descriptor.EnumDescriptor(
  name='ScanType',
  full_name='ScannerBuff.StartScan.ScanType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GREY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHASE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=525,
  serialized_end=556,
)
_sym_db.RegisterEnumDescriptor(_STARTSCAN_SCANTYPE)

_IMAGE_IMAGETYPE = _descriptor.EnumDescriptor(
  name='ImageType',
  full_name='ScannerBuff.Image.ImageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MONO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RGB', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=657,
  serialized_end=687,
)
_sym_db.RegisterEnumDescriptor(_IMAGE_IMAGETYPE)

_SETCALIBRATIONSTEP_CALIBRATIONSTEP = _descriptor.EnumDescriptor(
  name='CalibrationStep',
  full_name='ScannerBuff.setCalibrationStep.CalibrationStep',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOARD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROJECTOR_FOCUS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_FOCUS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_EXPOSURE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPUTE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=775,
  serialized_end=876,
)
_sym_db.RegisterEnumDescriptor(_SETCALIBRATIONSTEP_CALIBRATIONSTEP)

_CALIBRATIONPROBLEM_PROBLEM = _descriptor.EnumDescriptor(
  name='Problem',
  full_name='ScannerBuff.CalibrationProblem.Problem',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OBJECT_NOT_FOUND', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLATFORM_NOT_FOUND', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_CAMERA', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_PROJECTOR', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=956,
  serialized_end=1044,
)
_sym_db.RegisterEnumDescriptor(_CALIBRATIONPROBLEM_PROBLEM)


_POINTCLOUDWITHNORMALS = _descriptor.Descriptor(
  name='PointCloudWithNormals',
  full_name='ScannerBuff.PointCloudWithNormals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScannerBuff.PointCloudWithNormals.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='ScannerBuff.PointCloudWithNormals.vertices', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normals', full_name='ScannerBuff.PointCloudWithNormals.normals', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=107,
)


_POINTCLOUDWITHOUTNORMALS = _descriptor.Descriptor(
  name='PointCloudWithoutNormals',
  full_name='ScannerBuff.PointCloudWithoutNormals',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScannerBuff.PointCloudWithoutNormals.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='ScannerBuff.PointCloudWithoutNormals.vertices', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=165,
)


_POINTCLOUDPOINTNORMAL = _descriptor.Descriptor(
  name='PointCloudPointNormal',
  full_name='ScannerBuff.PointCloudPointNormal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScannerBuff.PointCloudPointNormal.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='ScannerBuff.PointCloudPointNormal.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=216,
)


_PROGRESSUPDATE = _descriptor.Descriptor(
  name='ProgressUpdate',
  full_name='ScannerBuff.ProgressUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='objectId', full_name='ScannerBuff.ProgressUpdate.objectId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='ScannerBuff.ProgressUpdate.amount', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=268,
)


_MESH = _descriptor.Descriptor(
  name='Mesh',
  full_name='ScannerBuff.Mesh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScannerBuff.Mesh.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vertices', full_name='ScannerBuff.Mesh.vertices', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normals', full_name='ScannerBuff.Mesh.normals', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indices', full_name='ScannerBuff.Mesh.indices', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=340,
)


_STARTCALIBRATION = _descriptor.Descriptor(
  name='StartCalibration',
  full_name='ScannerBuff.StartCalibration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ScannerBuff.StartCalibration.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STARTCALIBRATION_CALIBRATIONTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=342,
  serialized_end=463,
)


_STARTSCAN = _descriptor.Descriptor(
  name='StartScan',
  full_name='ScannerBuff.StartScan',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ScannerBuff.StartScan.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STARTSCAN_SCANTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=556,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='ScannerBuff.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ScannerBuff.Image.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='ScannerBuff.Image.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height', full_name='ScannerBuff.Image.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='ScannerBuff.Image.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IMAGE_IMAGETYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=559,
  serialized_end=687,
)


_SETCALIBRATIONSTEP = _descriptor.Descriptor(
  name='setCalibrationStep',
  full_name='ScannerBuff.setCalibrationStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='step', full_name='ScannerBuff.setCalibrationStep.step', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SETCALIBRATIONSTEP_CALIBRATIONSTEP,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=690,
  serialized_end=876,
)


_CALIBRATIONPROBLEM = _descriptor.Descriptor(
  name='CalibrationProblem',
  full_name='ScannerBuff.CalibrationProblem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='ScannerBuff.CalibrationProblem.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CALIBRATIONPROBLEM_PROBLEM,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=879,
  serialized_end=1044,
)

_STARTCALIBRATION.fields_by_name['type'].enum_type = _STARTCALIBRATION_CALIBRATIONTYPE
_STARTCALIBRATION_CALIBRATIONTYPE.containing_type = _STARTCALIBRATION
_STARTSCAN.fields_by_name['type'].enum_type = _STARTSCAN_SCANTYPE
_STARTSCAN_SCANTYPE.containing_type = _STARTSCAN
_IMAGE.fields_by_name['type'].enum_type = _IMAGE_IMAGETYPE
_IMAGE_IMAGETYPE.containing_type = _IMAGE
_SETCALIBRATIONSTEP.fields_by_name['step'].enum_type = _SETCALIBRATIONSTEP_CALIBRATIONSTEP
_SETCALIBRATIONSTEP_CALIBRATIONSTEP.containing_type = _SETCALIBRATIONSTEP
_CALIBRATIONPROBLEM.fields_by_name['type'].enum_type = _CALIBRATIONPROBLEM_PROBLEM
_CALIBRATIONPROBLEM_PROBLEM.containing_type = _CALIBRATIONPROBLEM
DESCRIPTOR.message_types_by_name['PointCloudWithNormals'] = _POINTCLOUDWITHNORMALS
DESCRIPTOR.message_types_by_name['PointCloudWithoutNormals'] = _POINTCLOUDWITHOUTNORMALS
DESCRIPTOR.message_types_by_name['PointCloudPointNormal'] = _POINTCLOUDPOINTNORMAL
DESCRIPTOR.message_types_by_name['ProgressUpdate'] = _PROGRESSUPDATE
DESCRIPTOR.message_types_by_name['Mesh'] = _MESH
DESCRIPTOR.message_types_by_name['StartCalibration'] = _STARTCALIBRATION
DESCRIPTOR.message_types_by_name['StartScan'] = _STARTSCAN
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['setCalibrationStep'] = _SETCALIBRATIONSTEP
DESCRIPTOR.message_types_by_name['CalibrationProblem'] = _CALIBRATIONPROBLEM

PointCloudWithNormals = _reflection.GeneratedProtocolMessageType('PointCloudWithNormals', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDWITHNORMALS,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.PointCloudWithNormals)
  ))
_sym_db.RegisterMessage(PointCloudWithNormals)

PointCloudWithoutNormals = _reflection.GeneratedProtocolMessageType('PointCloudWithoutNormals', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDWITHOUTNORMALS,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.PointCloudWithoutNormals)
  ))
_sym_db.RegisterMessage(PointCloudWithoutNormals)

PointCloudPointNormal = _reflection.GeneratedProtocolMessageType('PointCloudPointNormal', (_message.Message,), dict(
  DESCRIPTOR = _POINTCLOUDPOINTNORMAL,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.PointCloudPointNormal)
  ))
_sym_db.RegisterMessage(PointCloudPointNormal)

ProgressUpdate = _reflection.GeneratedProtocolMessageType('ProgressUpdate', (_message.Message,), dict(
  DESCRIPTOR = _PROGRESSUPDATE,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.ProgressUpdate)
  ))
_sym_db.RegisterMessage(ProgressUpdate)

Mesh = _reflection.GeneratedProtocolMessageType('Mesh', (_message.Message,), dict(
  DESCRIPTOR = _MESH,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.Mesh)
  ))
_sym_db.RegisterMessage(Mesh)

StartCalibration = _reflection.GeneratedProtocolMessageType('StartCalibration', (_message.Message,), dict(
  DESCRIPTOR = _STARTCALIBRATION,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.StartCalibration)
  ))
_sym_db.RegisterMessage(StartCalibration)

StartScan = _reflection.GeneratedProtocolMessageType('StartScan', (_message.Message,), dict(
  DESCRIPTOR = _STARTSCAN,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.StartScan)
  ))
_sym_db.RegisterMessage(StartScan)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.Image)
  ))
_sym_db.RegisterMessage(Image)

setCalibrationStep = _reflection.GeneratedProtocolMessageType('setCalibrationStep', (_message.Message,), dict(
  DESCRIPTOR = _SETCALIBRATIONSTEP,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.setCalibrationStep)
  ))
_sym_db.RegisterMessage(setCalibrationStep)

CalibrationProblem = _reflection.GeneratedProtocolMessageType('CalibrationProblem', (_message.Message,), dict(
  DESCRIPTOR = _CALIBRATIONPROBLEM,
  __module__ = 'ultiscantastic_pb2'
  # @@protoc_insertion_point(class_scope:ScannerBuff.CalibrationProblem)
  ))
_sym_db.RegisterMessage(CalibrationProblem)


# @@protoc_insertion_point(module_scope)
