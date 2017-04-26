#!/usr/bin/env python

#-----------------------------GCV Joy Mapper Node------------------------------#
import rospy
import time
import signal
import sys
import subprocess
from sensor_msgs.msg import Joy
from std_msgs.msg import Header
from gcv_motor_driver.msg import GCVControl
from edf.msg import Twist2DStamped

TAG = "GCV Joy Mapper Node:"

# SIGINT interrupt handler
def signal_handler(signal, frame):
    print ""
    print TAG,'Interrupt!'
    #Shutting down the motors

    print TAG,"Terminated"
    sys.exit(0)

#Joystick callback
def joy_callback(data):
    global pub
    global pub2
    global control_mode
    global joystick_type

    if (control_mode == "ctx24"):
        gain = 1.0
    else:
        gain = (data.axes[5] + 1)*(1 - 0.4)/(2.0) + 0.4

    # Tank mode
    if (control_mode == "tank"):
        if joystick_type == "ctx24":
            lm = gain*data.axes[1]
            rm = gain*data.axes[2]/0.25
            if rm>1.0:
                rm=1.0
        else:
            lm = gain*data.axes[1]
            rm = gain*data.axes[4]

        h = Header()
        h.stamp = rospy.Time.now()

        msg = GCVControl()
        msg.header = h
        #msg.left_track  = lm
        #msg.right_track = rm
        msg.left_track = lm
        msg.right_track = rm

        pub.publish(msg)

    # Differential drive mode
    if (control_mode == "differential_drive"):
        if joystick_type == "ctx24":
            omega = data.axes[0]
            velocity = data.axes[1]
            #velocity = data.axes[2]/0.25
            #if abs(velocity)>1.0:
                #velocity = velocity/abs(velocity)
        else:
            omega = gain*rotation_rate*data.axes[3]
            velocity = gain*data.axes[1]

        h = Header()
        h.stamp = rospy.Time.now()

        msg = Twist2DStamped()
        msg.header = h
        msg.velocity = velocity
        msg.omega = omega

        pub2.publish(msg)

if __name__ == '__main__':
    print TAG,"Started"
    signal.signal(signal.SIGINT, signal_handler)
    # Starting the node
    rospy.init_node('gcv_joy_mapper_node', anonymous=True)
    # Getting parameters
    control_mode = rospy.get_param("~control_mode","differential_drive")
    joystick_type = rospy.get_param("~joystick_type","default")
    print TAG, "Control Mode  -", control_mode
    print TAG, "Joystick Type -", joystick_type
    # Sucscribing
    rospy.Subscriber("/joy",Joy,joy_callback)
    pub = rospy.Publisher("/gcv_motor_driver",GCVControl, queue_size=10)
    pub2 = rospy.Publisher("/gcv_forward_kinematics_node/cmd", Twist2DStamped, queue_size=10)
    rospy.spin()

    print TAG,"Terminated"
