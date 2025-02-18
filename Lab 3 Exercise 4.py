# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 09:51:00 2023

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
dt = 0.001

def f(v):
    return B*(D*v) + C(D*v)**2




vx = 5
vy = 5

'''VELOCITY IN THE Y AXIS'''
tlisty = []
vys = [vy, ]
t = 0
while vy >= 0:        
    dvy = - g*dt - (b/m)*vy*dt
    vy = vy +dvy
    t = t + dt
    vys.append(vy)
    tlisty.append(t)
tmax = t

'''VELOCITY IN THE X AXIS'''
tlistx = []
vxs = []
t = 0 
while t <= tmax:
    dvx = - (b/m)*vx*dt
    vx = vx +dvx
    t = t + dt
    vxs.append(vx)
    tlistx.append(t)

plt.plot(vxs, vys)
plt.show()
    
