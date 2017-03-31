#!/usr/bin/env python

#-----------------------------GCV Joy Mapper Node------------------------------#
import rospy
import time
import signal
import sys
import subprocess
import pigpio
from sensor_msgs.msg import Joy
from std_msgs.msg import Header
from gcv_motor_driver.msg import GCVControl

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
    gain = (data.axes[5] + 1)*(1 - 0.3)/(2.0) + 0.3
    lm = gain*data.axes[1]
    rm = gain*data.axes[4]

    h = Header()
    h.stamp = rospy.Time.now()

    msg = GCVControl()
    msg.header = h
    msg.left_track  = lm
    msg.right_track = rm

    pub.publish(msg)

if __name__ == '__main__':
    print TAG,"Started"
    signal.signal(signal.SIGINT, signal_handler)
    rospy.init_node('gcv_joy_mapper_node', anonymous=True)
    rospy.Subscriber("/joy",Joy,joy_callback)
    pub = rospy.Publisher("/gcv_motor_driver",GCVControl, queue_size = 10)
    rospy.spin()

    print TAG,"Terminated"
