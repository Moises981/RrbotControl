#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import rosbag

bag = rosbag.Bag('/home/pc/RrbotControl/src/data.bag')
t, data = [], []
for topic, msg, tm in bag.read_messages(topics=['/dynamic_data']):
    t.append(tm.secs+tm.nsecs/1000000000.0)
    data.append(msg.data)
bag.close()
m = np.array(data)


ax1 = plt.subplot2grid(shape=(2,6), loc=(0,0), colspan=2)
ax2 = plt.subplot2grid((2,6), (0,2), colspan=2)
ax3 = plt.subplot2grid((2,6), (0,4), colspan=2)
ax4 = plt.subplot2grid((2,6), (1,0), colspan=2)
ax5 = plt.subplot2grid((2,6), (1,2), colspan=2)
ax6 = plt.subplot2grid((2,6), (1,4), colspan=2)


x2, y2, x3, y3 = m[:,0], m[:,1], m[:,6], m[:,7]
ax1.plot(x2,y2,x3,y3)
ax1.axis('equal')
ax1.legend(['$CM_2$','$CM_3$'])
ax1.set_title('Trajectory of the center of mass')

th2, th3 = m[:,2], m[:,8]
ax2.plot(t,th2,t,th3)
ax2.legend(['$th_2$','$th_3$'])
ax2.set_title('Orientation of the link')

vx2, vy2, vx3, vy3 = m[:,3], m[:,4], m[:,9], m[:,10]
ax3.plot(t,vx2,t,vy2,t,vx3,t,vy3)
ax3.legend(['$v_{x2}$','$v_{y2}$','$v_{x3}$','$v_{y3}$'])
ax3.set_title('Linear velocity of the center of mass')

w2, w3 = m[:,5], m[:,11]
ax4.plot(t,w2,t,w3)
ax4.legend(['$w_2$','$w_3$'])
ax4.set_title('Angular velocity XY of the center of mass')

v2 = np.sqrt(np.square(m[:,3])+np.square(m[:,4]))
v3 = np.sqrt(np.square(m[:,9])+np.square(m[:,10]))
ax5.plot(t,v2,t,v3)
ax5.legend(['${v2}$','${v3}$'])
ax5.set_title('Linear velocity of the center of mass')

pe, ke = m[:,12], m[:,13]
pe_ref = pe[-1]
ax6.plot(t,pe-pe_ref,t,ke)
ax6.set_title('Energy')
ax6.legend(['potential energy','kinetic energy'])

plt.show()
