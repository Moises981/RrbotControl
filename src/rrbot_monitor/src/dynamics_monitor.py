#!/usr/bin/env python

import math, rospy, numpy as np

from gazebo_msgs.msg import LinkStates
from std_msgs.msg import Float32MultiArray

def pose2d(pose):
    x, y = pose.position.x, pose.position.z
    theta = 2 * math.atan2(pose.orientation.y, pose.orientation.w)
    return (x, y, theta)

def twist2d(twist):
    return (twist.linear.x, twist.linear.z, twist.angular.y)

def callback(msg_in):
    global pub
    
    x2, y2, th2 = pose2d(msg_in.pose[2])
    vx2, vy2, w2 = twist2d(msg_in.twist[2])
    x3, y3, th3 = pose2d(msg_in.pose[3])
    vx3, vy3, w3 = twist2d(msg_in.twist[3])
    #print(x2)
    print(y2)
    #print(x3)
    print(y3)
    # xc2 = 
    # yc2 = 
    # xc3 = 
    # yc3 = 
    # vxc2 = 
    # vyc2 = 
    # vxc3 = 
    # vyc3 = 
    # m = 1.0
    # g = 9.81
    # I = 0.084
    # pe = 
    # ke = 
    
    # data = [xc2,yc2,th2,vxc2,vyc2,w2,xc3,yc3,th3,vxc3,vyc3,w3,pe,ke]
    # msg_out = Float32MultiArray(data=data)
    # pub.publish(msg_out)

if __name__ == '__main__':
    rospy.init_node('energy_monitor', anonymous=True)
    sub = rospy.Subscriber('/gazebo/link_states', LinkStates, callback)
    pub = rospy.Publisher('/dynamic_data', Float32MultiArray, queue_size=10)
    rospy.spin()