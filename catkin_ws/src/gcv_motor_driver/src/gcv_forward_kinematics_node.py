#!/usr/bin/env python

#------------------------GCV Forward Kinematics Node---------------------------#

import rospy
import signal
import sys
from std_msgs.msg import Header
from gcv_motor_driver.msg import GCVControl
from edf.msg import Twist2DStamped

def signal_handler(signal, frame):
    print ""
    print TAG,'Interrupt!'

    print TAG,"Terminated"
    sys.exit(0)

# MEssage callback
def onNewMessage(data):
    global pub

    global v_gain
    global r_gain
    global trim

    if (trim >= 0 ):
        lm = (v_gain*data.velocity) - (r_gain*data.omega)
        rm = (1.0 + trim)*((v_gain*data.velocity) + (r_gain*data.omega))
    else:
        lm = (1.0 - trim)*(v_gain*data.velocity) - (r_gain*data.omega)
        rm = ((v_gain*data.velocity) + (r_gain*data.omega))

    if (abs(lm)>1.0):
        rm = rm / abs(lm)
        lm = lm/abs(lm)
    if (abs(rm)>1.0):
        lm = lm / abs(rm)
        rm = rm/abs(rm)

    h = Header()
    h.stamp = rospy.Time.now()

    msg = GCVControl()
    msg.header = h
    msg.left_track = lm
    msg.right_track = rm

    pub.publish(msg);

# --------------------------------- MAIN --------------------------------------#
if __name__ == '__main__':
    TAG = "GCV Forward Kinematics Node:"
    signal.signal(signal.SIGINT, signal_handler)

    print TAG,"Started"

    # Starting the Node
    rospy.init_node("gcv_forward_kinematics_node")
    # Getting parameters
    trim = rospy.get_param("~trim", 0.0)     # Calibration trim: -1.00 .. 1.00
    v_gain = rospy.get_param("~v_gain",1.00) # Velocity gain:     0.00 .. 1.00
    r_gain = rospy.get_param("~r_gain",1.00) # Rotation gain:     0.00 .. 1.00
    print TAG,"trim =",trim
    print TAG,"v_gain =",v_gain
    print TAG,"r_gain =",r_gain

    # Subscriber
    rospy.Subscriber("~cmd", Twist2DStamped, onNewMessage)
    pub = rospy.Publisher("/gcv_motor_driver", GCVControl, queue_size = 10)
    rospy.spin()

    print TAG,"Terminated"
