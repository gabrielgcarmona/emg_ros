#!/usr/bin/env python
import rospy
import numpy as np
import pickle
from statsmodels.tsa.ar_model import AR
from sklearn.datasets.samples_generator import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.svm import *
from numpy import convolve as conv
from scipy.signal import *
from sklearn.svm import SVC
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from std_msgs.msg import Int32
from std_msgs.msg import Float64MultiArray


global pub
global svm
global sc
svm = pickle.load(open('/home/gabriel/catkin_ws/src/emg_ros/scripts/maquina.sav', 'rb'))
sc = pickle.load(open('/home/gabriel/catkin_ws/src/emg_ros/scripts/scaler.sav', 'rb'))
pub = rospy.Publisher('prediction', Int32, queue_size=10)

def callback(data):
    global pub
    global svm
    global sc
    dados =np.array(data.data).reshape(1,-1)
    params = sc.transform(dados)
    prediction = svm.predict(params)
    pub.publish(Int32(prediction))


def predictor():
    rospy.init_node('predictor', anonymous=True)
    rospy.Subscriber('extracted', Float64MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        predictor()
    except rospy.ROSInterruptException:
        pass