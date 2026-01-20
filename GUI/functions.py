"""
A program with three functions
"""

import math
from math import pi


print("""
1.) Solve equation
2.) Even numbers

""")
choice = input("Enter option: ")


def even():
    number = []
    user = int(input("Enter number: "))
    if user /2:
        number.append(user)
        print(number)
    
    else:
        print("Number is not even")

def option():
    print("""
    1.) T = 2pi * l/g
    2.) F = GMm/r**2
    3.) E = mc**2          
    """)
    calc()
   
def calc():
    choice2 = input("Enter choice: ")
    if choice2 == "1":
        l = float(input("Enter lenght: "))
        g = float(input("Enter g: "))
        t = 2*pi*l/g
        print(t)   

    if choice2 == "2":
        G = 9.81
        M = float(input("Enter M: "))
        m = float(input("Enter m: "))
        r = float(input("Enter r: ")) 
        f = G*M*m/r**2
        print(f)

    if choice2 == "3":
        m2 = float(input("Enter m: "))
        c = float(input("Enter C: "))
        E = m2*c**2
        print(E)



   



if choice == "2":
    even()

if choice == "1":
    option()
    

