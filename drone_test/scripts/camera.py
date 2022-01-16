#!/usr/bin/env python3

from sensor_msgs.msg import CompressedImage
import rospy

def talker():
    global pub, velocity_msg
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rospy.Subscriber('/camera/rgb/image_raw/compressedDepth', Range, hieght_control)
    rospy.init_node('fly_drone', anonymous=True)
    rate = rospy.Rate(10)
    velocity_msg = CompressedImage()
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


