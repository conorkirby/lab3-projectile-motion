# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:00:59 2023

@author: Conor Kirby
"""
import numpy as np
import matplotlib.pyplot as plt

B = 1.6*(10**-4)
C = 0.25

D = 0.07 #diameter
v = np.linspace(0, 0.02, 150)

b = B*D
c = C*D*D

def f(v):
    return B*(D*v) + C(D*v)**2

plt.plot(D*v, c*v**2)
plt.plot(D*v, b*v)
plt.grid()

plt.xlabel("Dv (m^2/s)")
plt.ylabel("f (N)")
plt.title("f(v) as a function of the velocity magnitude")
plt.legend(["Quadratic Term", "Linear Term"])
plt.axis([0, 0.0012, 0, 3*(10)**-7])
#plt.savefig('C:/Users/Conor Kirby/OneDrive/Desktop/Computational Lab/Lab 3/bV and cV^2.pdf')
plt.show()

#for example when D = 7cm, v = 5 m/s, Dv = 0.35, wayyy bigger than intersection
#in report make table for the 3 cases and see how little the linear contributes

#baseball
D = 0.07
v = 5
print(D*v) #0.35000000000000003 way bigger than intersection point hence quadratic more dominant

#tiny drop of oil
D = 1.5e-6
v = 5e-5
print(D*v) #7.5e-11 way smaller than intersection point hence linear more dominant

#raindrop
D = 0.001
v = 1
print(D*v) #both linear and quadratic are contributing