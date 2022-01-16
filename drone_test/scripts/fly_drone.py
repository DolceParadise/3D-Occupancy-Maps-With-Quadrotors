#!/usr/bin/env python3

import rospy 
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Range


def talker():
    global pub, velocity_msg
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber('/sonar_height', Range, hieght_control)
    rospy.init_node('fly_drone', anonymous=True)
    rate = rospy.Rate(10)
    velocity_msg = Twist()
    rospy.spin()


def hieght_control(msg):
    global pub, velocity_msg
    sonar_data = msg.range
    velocity_msg.linear.z = (1.5- sonar_data)
    pub.publish(velocity_msg)
    print("sonar value : ", sonar_data)



if __name__=="__main__":
    try:
        talker()
    except rospy.ROSInterruptException():
        print("kuch garbar hai")
        pass


