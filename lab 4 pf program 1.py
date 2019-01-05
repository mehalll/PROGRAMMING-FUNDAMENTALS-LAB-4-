#PROGRAM TO CALCULATE QUADRATIC EQUATIONS

import math


a,b,c=int(input("Enter the coefficients of a, b and c seperated by commas: ")


d = b**2-4*a*c #descriminent
          
if d < 0:
    print ("This equation has no real solution")
elif d == 0:
    x = (-b+math.sqrt(b**2-4*a*c)/2*a
    print ("this equation has one solution", x1)
else:
     x1 = (-b+math.sqrt((b**2)-(4*a*c))))/2*a
     x2 = (-b-math.sqrt((b**2)-(4*a*c)))))/2*a
     print("This equation has two solutions: " ,x1 , "or" ,x2)    
