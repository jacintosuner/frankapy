# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feedback_controller_params_msg.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$feedback_controller_params_msg.proto\"p\n+CartesianImpedanceFeedbackControllerMessage\x12!\n\x19translational_stiffnesses\x18\x01 \x03(\x01\x12\x1e\n\x16rotational_stiffnesses\x18\x02 \x03(\x01\"q\n\"ForceAxisFeedbackControllerMessage\x12\x1f\n\x17translational_stiffness\x18\x01 \x02(\x01\x12\x1c\n\x14rotational_stiffness\x18\x02 \x02(\x01\x12\x0c\n\x04\x61xis\x18\x03 \x03(\x01\"K\n\'JointImpedanceFeedbackControllerMessage\x12\x0f\n\x07k_gains\x18\x01 \x03(\x01\x12\x0f\n\x07\x64_gains\x18\x02 \x03(\x01\"d\n*InternalImpedanceFeedbackControllerMessage\x12\x1c\n\x14\x63\x61rtesian_impedances\x18\x01 \x03(\x01\x12\x18\n\x10joint_impedances\x18\x02 \x03(\x01\"\xc0\x01\n&ForcePositionFeedbackControllerMessage\x12\x19\n\x11position_kps_cart\x18\x01 \x03(\x01\x12\x16\n\x0e\x66orce_kps_cart\x18\x02 \x03(\x01\x12\x1a\n\x12position_kps_joint\x18\x03 \x03(\x01\x12\x17\n\x0f\x66orce_kps_joint\x18\x04 \x03(\x01\x12\x11\n\tselection\x18\x05 \x03(\x01\x12\x1b\n\x13use_cartesian_gains\x18\x06 \x02(\x08\"\x8a\x01\n$JointTorqueFeedbackControllerMessage\x12\x11\n\tselection\x18\x01 \x03(\x01\x12\x16\n\x0eremove_gravity\x18\x02 \x03(\x01\x12\x15\n\rjoint_torques\x18\x03 \x03(\x01\x12\x0f\n\x07k_gains\x18\x04 \x03(\x01\x12\x0f\n\x07\x64_gains\x18\x05 \x03(\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feedback_controller_params_msg_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CARTESIANIMPEDANCEFEEDBACKCONTROLLERMESSAGE._serialized_start=40
  _CARTESIANIMPEDANCEFEEDBACKCONTROLLERMESSAGE._serialized_end=152
  _FORCEAXISFEEDBACKCONTROLLERMESSAGE._serialized_start=154
  _FORCEAXISFEEDBACKCONTROLLERMESSAGE._serialized_end=267
  _JOINTIMPEDANCEFEEDBACKCONTROLLERMESSAGE._serialized_start=269
  _JOINTIMPEDANCEFEEDBACKCONTROLLERMESSAGE._serialized_end=344
  _INTERNALIMPEDANCEFEEDBACKCONTROLLERMESSAGE._serialized_start=346
  _INTERNALIMPEDANCEFEEDBACKCONTROLLERMESSAGE._serialized_end=446
  _FORCEPOSITIONFEEDBACKCONTROLLERMESSAGE._serialized_start=449
  _FORCEPOSITIONFEEDBACKCONTROLLERMESSAGE._serialized_end=641
  _JOINTTORQUEFEEDBACKCONTROLLERMESSAGE._serialized_start=644
  _JOINTTORQUEFEEDBACKCONTROLLERMESSAGE._serialized_end=782
# @@protoc_insertion_point(module_scope)
