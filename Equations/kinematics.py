"""
kinematics
"""

from math import sqrt

velocity = float(input("Enter velocity: "))
acceleration = float(input("Enter acceleration: "))
diplacement = float(input("Enter displacement: "))

v = velocity**2+2*acceleration*diplacement
vfinal = sqrt(v)

print(vfinal)

