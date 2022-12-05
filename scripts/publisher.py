#!/home/bolt/miniconda3/bin/python
# license removed for brevity
import rospy
from std_msgs.msg import String
import time
from typing import Optional

import serial


def talker():
    ser = serial.Serial(
        # Serial Port to read the data from
        port='/dev/ttyUSB0',
 
        #Rate at which the information is shared to the communication channel
        baudrate = 115200,
   
        #Applying Parity Checking (none in this case)
        parity=serial.PARITY_NONE,
 
       # Pattern of Bits to be read
        stopbits=serial.STOPBITS_ONE,
     
        # Total number of bits to be read
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

    pub = rospy.Publisher('IMU/data', String, queue_size=10)
    rospy.init_node('usb_serial_pub', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        data = ser.readline() 
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass