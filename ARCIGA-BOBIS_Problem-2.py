#Import libraries
import numpy as np

print('Calculating for the center, radius, and a vector given three points on a circle') 
X1 = float(input("Input X-Coordinate of First Point: "))
Y1 = float(input("Input Y-Coordinate of First Point: "))
X2 = float(input("Input X-Coordinate of Second Point: "))
Y2 = float(input("Input Y-Coordinate of Second Point: "))
X3 = float(input("Input X-Coordinate of Third Point: "))
Y3 = float(input("Input Y-Coordinate of Third Point: "))

#General equation of a circle: (x^2)+(y^2)+Dx+Ex+F=0
#Matrix R is the coefficient matrix of Dx+Ex+F from the general formula
R=np.array([(X1,Y1,1),(X2,Y2,1),(X3,Y3,1)])
 
#From the general equation, the values for C1, C2, C3 are '(x^2)+(y^2)' transferred on the other side of the equation
C1= -((X1**2)+(Y1**2));
C2= -((X2**2)+(Y2**2));
C3= -((X3**2)+(Y3**2));

#Solving for the inverse of Matrix R:
I=np.linalg.inv(R)

#Multiplying the inverse of Matrix R to Matrix C will give as rref(R)
#The rows of rref(R) corresponds to the values of D,E,F
D=I[0,0]*(C1)+I[0,1]*(C2)+I[0,2]*(C3)
E=I[1,0]*(C1)+I[1,1]*(C2)+I[1,2]*(C3)
F=I[2,0]*(C1)+I[2,1]*(C2)+I[2,2]*(C3)

#Standard equation of a circle: ((x-h)^2)+((y-k)^2)=(r^2)
#center(h,k) and r can be computed by completing the square method
h=round(-(D/2),3)
k=round(-(E/2),3)
r=round((abs(-(F)+(h**2)+(k**2)))**(1/2),3) 

print('Center(h,k): (',h,',',k,')')
print('Radius: ',r)
print('Vector[D,E,F]: [',round(D,3),',',round(E,3),',',round(F,3),']')