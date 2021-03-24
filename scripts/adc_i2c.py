#!/usr/bin/env python
import rospy
import Adafruit_ADS1x15
from std_msgs.msg import Int32

global adc
adc = Adafruit_ADS1x15.ADS1015()

def main():
    global adc

    pub = rospy.Publisher('dados', Int32, queue_size=10)
    rospy.init_node('adc', anonymous=True)
    rate = rospy.Rate(1600)
    
    adc.start_adc(0, gain=1)
    while not rospy.is_shutdown():
        dados = adc.get_last_result()
        pub.publish(Int32(dados))
        rate.sleep()
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        adc.stop_adc()
