
#Write a Python program to convert kilometers to miles?
kilometers=float(input("enter the value in kilometers: "))
conversion_factor=0.621371
miles=kilometers*conversion_factor
print("%s kilometers in miles is %s"%(kilometers,miles))

#Write a Python program to convert Celsius to Fahrenheit?
celsius=float(input("enter the value in celsius: "))
Fahrenheit= (celsius * 1.8) + 32
print("%s celsius in Fahrenheit is %s" %(celsius,Fahrenheit))

#Write a Python program to display calendar?
import calendar
yy=int(input('enter the year: '))
mm=int(input("enter the month: "))
print(calendar.month(yy,mm))

#Write a Python program to solve quadratic equation?
import cmath
a=int(input("enter the first coeffient: "))
b=int(input("enter the second coewffient: "))
c=int(input("enter the third coeffient: "))
d=(b**2)-(4*a*c)
sol1=(-b+cmath.sqrt(d))/(2*a)
sol2=(-b-cmath.sqrt(d))/(2*a)
print("solution 1 of the given quadratic equation is: ",sol1)
print("solution 2 of the given quadratic equation is: ",sol2)

#Write a Python program to swap two variables without temp variable?
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
a=a+b
b=a-b
a=a-b
print("the value of a is: ",a)
print("the value of b is: ",b)

