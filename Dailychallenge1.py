#Write a function in Python that accepts one numeric parameter.
#This parameter will be the measure of an angle in radians. 
#The function should convert the radians into degrees and then return that value.
#While you might find a Python library to do this for you, you should write the function yourself. 
# One hint you get is that you’ll need to use Pi in order to solve this problem. 
# You can import the value for Pi from Python’s math module.


#Note that formula for Radians= Degrees×π / 180
import math
def radianToDegree(radians):
   # radians = (Degree * math.pi)/180
    degree = (radians * 180) / math.pi 

    return degree

degree = float(input("Enter Value for Degree: "))
print(radianToDegree(degree))

    




















