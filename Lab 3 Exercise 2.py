# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:09:49 2023

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
tmax = 1
t = 0
vy = 0
vylist = []
tlist = []

def f(v):
    return B*(D*v) + C(D*v)**2

tlista = []
vysa = []
t = 0 
tmax = 1
vy_a = 0
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
plt.plot(tlist, vylist, "k")
#plt.axis([0,1,-.7, 0])
plt.grid()
plt.xlabel("time (s)")
plt.ylabel("Y Velocity (m/s)")
plt.title("Reaching Terminal Velocity Numerical vs Analytical")
plt.show
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 3/tvelocity,1.0472e-9.pdf')

def vya(t):
    return (m*g)/b * (np.exp(-b*t/m) - 1) 
tlista = []
vysa = []
t = 0 
tmax = 1
vy_a = 0
while t <= tmax:
    vy_a = vya(t)
    t = t + dt
    vysa.append(vy_a)
    tlista.append(t)
    
plt.plot(tlista, vysa, "--r")
plt.legend(["Numerical", "Analytical"])
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 3/nva2.pdf')

plt.show()
#print(tlista)


error = []
for i in range(len(tlista)):
    error.append(-(vysa[i]-vylist[i])/vysa[i])
    
plt.plot(tlist, error)
plt.title("Error")
plt.xlabel("time (s)")
plt.ylabel("Error between numerical and analyltical Vy")
plt.grid()
plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 3/error2.pdf')
plt.show()



dt = 0.001

airtimes = []
ylist = []
vys = []
masses = np.arange(0.000000000001, 10, 1e-1)

for i in range(0,len(masses)):
    #print(masses[i])
    t = 0
    y = 5
    vy = 0
    while y >= 0:
        dvy = -g*dt - (b/masses[i])*vy*dt
        vy = vy + dvy
        dy = vy*dt
        y = y + dy
        
        t = t + dt
        #print(t)
    #print(t)
    airtimes.append(t)
plt.show()        
#print(airtimes)  
#print(masses)
plt.plot(airtimes, masses)
