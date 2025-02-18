# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 22:37:38 2023

@author: Conor Kirby
"""

import numpy as np
import matplotlib.pyplot as plt

B = 1.6*(10**-4)
C = 0.25
D = 1e-4

b = B*D
c = C*D*D

g = 9.8




m = 1.0472e-9
dt = 0.01
tmax = 1
t = 0
vy = 0
vylist = []
tylist = []

def f(v):
    return B*(D*v) + C(D*v)**2

vysa = []
t = 0 
tmax = 1
vy_a = 0
while t <= tmax:
    dvy = -g*dt - (b/m)*vy*dt
    vy = vy +dvy
    t = t + dt
    vylist.append(vy)
    tylist.append(t)

t = 0
vx = 0
vxlist = []
txlist = []


while t <= tmax:
    dvx = - (b/m)*vy*dt
    vx = vx +dvx
    t = t + dt
    vxlist.append(vx)
    txlist.append(t)

plt.plot(vxlist, vylist)
#plt.axis([0,1,-.7, 0])
plt.grid()
plt.xlabel("time (s)")
plt.ylabel("Y Velocity (m/s)")
plt.title("Reaching Terminal Velocity")
plt.show
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 3/yvsx.pdf')