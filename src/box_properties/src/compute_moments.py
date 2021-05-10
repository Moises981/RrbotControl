#!/usr/bin/env python
import rospy
from math import pow

m = 2
w = 0.4
d = 0.5
h = 0.3

Ih = m*(pow(w,2)+pow(d,2))/12
Iw = m*(pow(d,2)+pow(h,2))/12
Id = m*(pow(w,2)+pow(h,2))/12

print("Ih: "+str(Ih))
print("Iw: "+str(Iw))
print("Id: "+str(Id))