
#Write a Python program to print "Hello Python"?
a="Hello Python"
print(a)
#Write a Python program to do arithmetical operations addition and division.?
a=int(input("enter the first number"))
b=int(input("enter the first number"))
c=a+b
d=a*b
print("the sum of the numbers are: ",c)
print("the product  of the numbers are: ",d)
#Write a Python program to find the area of a triangle?
Base=int(input("enter the length of the base of the triangle"))
Height=int(input("enter the height of the triangle"))
Area=(1/2)*Base*Height
print("The area of the triangle is: ",Area)

#Write a Python program to swap two variables?
a=str(input("enter the first word"))
b=str(input("enter the second word"))
a,b=b,a

print("The value of a after swapping is : ",a)
print("The value of b after swapping is: ",b)

#Write a Python program to generate a random number?
import random
print(random.randint(0,10))