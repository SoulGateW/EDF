#!/usr/bin/env python

#----------------------------GCV Motor Driver Node-----------------------------#
import rospy
import time
import signal
import sys
import subprocess
import pigpio
from sensor_msgs.msg import Joy
from gcv_motor_driver.msg import GCVControl

# GCV motor control pins
GCV_L1 = 12  # Left motor PWM enabled pin
GCV_L2 = 26
GCV_R1 = 13  # Right motor PWM enabled pin
GCV_R2 = 19

TAG = "GCV Motor Driver Node:"

# Stopping motors
def stop_motors():
    global pi
    pi.write(GCV_L1, 0)
    pi.write(GCV_L2, 0)
    pi.write(GCV_R1, 0)
    pi.write(GCV_R2, 0)
    print TAG,"Motors are stopped"

# SIGINT interrupt handler
def signal_handler(signal, frame):
    global pi

    print ""
    print TAG,'Interrupt!'
    #Shutting down the motors
    stop_motors()

    print TAG,"Terminated"
    sys.exit(0)

#Joystick callback
def control_callback(data):
    global pi

    lm = data.left_track
    rm = data.right_track
    # Conrolling the tracks via both RPi hardware PWMs
    if (abs(lm) < 0.1):
        pi.write(GCV_L1,0)
        pi.write(GCV_L2,0)
    elif (lm < 0):
        pi.hardware_PWM(GCV_L1, 100, round(abs(lm)*1000000))
        pi.write(GCV_L2, 0)
    else:
        pi.hardware_PWM(GCV_L1, 100, round((1.0-abs(lm))*1000000))
        pi.write(GCV_L2, 1)

    if (abs(rm) < 0.1):
        pi.write(GCV_R1,0)
        pi.write(GCV_R2,0)
    elif (rm < 0):
        pi.hardware_PWM(GCV_R1, 100, round(abs(rm)*1000000))
        pi.write(GCV_R2, 0)
    else:
        pi.hardware_PWM(GCV_R1, 100, round((1.0-abs(rm))*1000000))
        pi.write(GCV_R2, 1)

#----------------------------------- MAIN -------------------------------------#
if __name__ == '__main__':
    print TAG,"Started"
    signal.signal(signal.SIGINT, signal_handler)

    # Setting up motors
    print TAG,"Setting up motors"

    pi = pigpio.pi()

    pi.set_mode(GCV_L1,pigpio.OUTPUT)
    pi.set_mode(GCV_L2,pigpio.OUTPUT)
    pi.set_mode(GCV_R1,pigpio.OUTPUT)
    pi.set_mode(GCV_R2,pigpio.OUTPUT)

    pi.write(GCV_L1, 0)
    pi.write(GCV_L2, 0)
    pi.write(GCV_R1, 0)
    pi.write(GCV_R2, 0)

    #gcv_motor_driver_node_rpi node
    rospy.init_node("gcv_motor_driver_node_rpi")
    rospy.Subscriber("/gcv_motor_driver",GCVControl,control_callback)
    rospy.spin()

stop_motors()
print TAG,"Terminated"
