"""
Universal Gravitation
"""

GRAVITATION = 9.81
mass1 = float(input("Enter mass1: "))
mass2 = float(input("Enter mass2: "))
r = float(input("Enter radius: "))

f = GRAVITATION*mass1*mass2/r**2
print(f)