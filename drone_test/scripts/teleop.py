#!/usr/bin/env python3

import rospy 
from geometry_msgs.msg import Twist
import roslib
import sys, select, termios, tty
import threading

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

msg = """

v initial speed = 0.3

w go upward with speed v
s go downward with speed v
a rotate clockwise with speed v
d rotate anti - clockwise with speed v
t go forward with speed v
g go backward with speed v
f go left with speed v
h go right with speed v
x sudden stop
c increase v(speed) by 0.1
v decrease v(speed) by 0.1


"""

if __name__=="__main__":
    try:
        settings = termios.tcgetattr(sys.stdin)
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.init_node('fly_drone', anonymous=True)
        rate = rospy.Rate(10)
        v = 0.3
        a = 0
        while True:
            if a%10==0:
            	print(msg)
            vel = Twist()
            key = getKey()
            if key == "w":
                vel.linear.z = v
                print("up")
            elif key == "s":
                vel.linear.z = -v
                print("down")
            elif key == "a":
                vel.angular.z = v
                print("rotate left")
            elif key == "d":
                vel.angular.z = -v
                print("rotate right")
            elif key == "t":
                vel.linear.x = v
                print("forward")
            elif key == "g":
                vel.linear.x = -v
                print("back")
            elif key == "f":
                vel.linear.y = v
                print("left")
            elif key == "h":
                vel.linear.y = -v
                print("right")
            elif key == "x":
                vel.linear.x = 0
                vel.linear.y = 0
                vel.linear.z = 0
                vel.angular.x = 0
                vel.angular.y = 0
                vel.angular.z = 0
                print("stop")
            elif key == "c":
                v += 0.1
                print("vel increase")
            elif key == "v":
                v -= 0.1
                print("vel decrease")
            elif key == "m":
                break
            pub.publish(vel)
            a+=1
    except rospy.ROSInterruptException():
        print("kuch garbar hai")
        pass




