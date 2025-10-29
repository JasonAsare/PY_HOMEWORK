"""
Centripetal force
"""

mass = float(input("Enter mass: "))
velocity = float(input("Enter speed: "))
radius = float(input("Enter radius: "))

f = mass*velocity**2/radius
print(f)