; Auto-generated. Do not edit!


(cl:in-package gcv_motor_driver-msg)


;//! \htmlinclude GCVControl.msg.html

(cl:defclass <GCVControl> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (left_track
    :reader left_track
    :initarg :left_track
    :type cl:float
    :initform 0.0)
   (right_track
    :reader right_track
    :initarg :right_track
    :type cl:float
    :initform 0.0))
)

(cl:defclass GCVControl (<GCVControl>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GCVControl>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GCVControl)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gcv_motor_driver-msg:<GCVControl> is deprecated: use gcv_motor_driver-msg:GCVControl instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <GCVControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gcv_motor_driver-msg:header-val is deprecated.  Use gcv_motor_driver-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'left_track-val :lambda-list '(m))
(cl:defmethod left_track-val ((m <GCVControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gcv_motor_driver-msg:left_track-val is deprecated.  Use gcv_motor_driver-msg:left_track instead.")
  (left_track m))

(cl:ensure-generic-function 'right_track-val :lambda-list '(m))
(cl:defmethod right_track-val ((m <GCVControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gcv_motor_driver-msg:right_track-val is deprecated.  Use gcv_motor_driver-msg:right_track instead.")
  (right_track m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GCVControl>) ostream)
  "Serializes a message object of type '<GCVControl>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'left_track))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'right_track))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GCVControl>) istream)
  "Deserializes a message object of type '<GCVControl>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'left_track) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'right_track) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GCVControl>)))
  "Returns string type for a message object of type '<GCVControl>"
  "gcv_motor_driver/GCVControl")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GCVControl)))
  "Returns string type for a message object of type 'GCVControl"
  "gcv_motor_driver/GCVControl")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GCVControl>)))
  "Returns md5sum for a message object of type '<GCVControl>"
  "d2e51d95c55716bb1993b7d66b71eb5a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GCVControl)))
  "Returns md5sum for a message object of type 'GCVControl"
  "d2e51d95c55716bb1993b7d66b71eb5a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GCVControl>)))
  "Returns full string definition for message of type '<GCVControl>"
  (cl:format cl:nil "Header header~%float32 left_track~%float32 right_track~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GCVControl)))
  "Returns full string definition for message of type 'GCVControl"
  (cl:format cl:nil "Header header~%float32 left_track~%float32 right_track~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GCVControl>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GCVControl>))
  "Converts a ROS message object to a list"
  (cl:list 'GCVControl
    (cl:cons ':header (header msg))
    (cl:cons ':left_track (left_track msg))
    (cl:cons ':right_track (right_track msg))
))
