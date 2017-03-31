
(cl:in-package :asdf)

(defsystem "gcv_motor_driver-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "GCVControl" :depends-on ("_package_GCVControl"))
    (:file "_package_GCVControl" :depends-on ("_package"))
  ))