#!/usr/bin/env python
import rospy
from gazebo_utils.services import (set_pose, get_pose)
import sys
import time

#Move box in x Axis
steps = int(sys.argv[1])

for y in range(0,steps):
    p = get_pose('cardboard_box')
    p.position.y += 0.01
    set_pose('cardboard_box', p)
    time.sleep(0.1)
