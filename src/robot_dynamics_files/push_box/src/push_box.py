#! /usr/bin/env python
import rospy
from gazebo_utils.services import (set_pose, get_pose)

#Move box 5 cm
p = get_pose('cardboard_box')
p.position.x -= 0.05
set_pose('cardboard_box', p)