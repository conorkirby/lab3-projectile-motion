# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 11:34:22 2023

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


def f(v):
    return B*(D*v) + C(D*v)**2



mlist = [1.1e-9, 2e-9, 5e-9, 2e-8, 2e-2, 2, 20]
for m in mlist:
    dt = 0.01
    tmax = 1
    t = 0
    vy= 0
    vylist = [0,]
    tlist = [0,]
    
    while t <= tmax:
        dvy = -g*dt - (b/m)*vy*dt
        vy = vy +dvy
        t = t + dt
        vylist.append(vy)
        tlist.append(t)
        
        #print(t)
        #print(vy)
    #print(vylist)  
    #print(tlist)  
    plt.plot(tlist, vylist, label = f"{m} kg")
    #plt.axis([0,1,-.7, 0])
    plt.grid()
    plt.legend()
    plt.xlabel("time (s)")
    plt.ylabel("Y Velocity (m/s)")
    plt.title("Reaching Terminal Velocity")

#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 3/finaltvelocity,range of m.pdf')
plt.show()

