#!/usr/bin/env python

import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import Int32MultiArray


global pub
global parameters

parameters=Float64MultiArray()
parameters.data = 2 * [0]
counter = 0
pub = rospy.Publisher('extracted', Float64MultiArray, queue_size=10)
def callback(data):
    global pub  
    global parameters
    x=data.data - np.mean(data.data)
    parameters.data[0] = np.mean(np.abs(x))
    parameters.data[1] = np.square(np.sum(x**2)/len(x))
    pub.publish(parameters)
    


def extraction():
    rospy.init_node('extraction', anonymous=True)
    rospy.Subscriber('data_window', Int32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        extraction()
    except rospy.ROSInterruptException:
        pass