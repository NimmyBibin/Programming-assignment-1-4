
#Write a Python Program to Find the Factorial of a Number?
def fact(n):
    factorial=1 if (n==1 or n==0) else n*fact(n-1)
    return factorial
print(fact(5))

#Write a Python Program to Display the multiplication Table?
num=int(input("enter the number"))
for i in range(1,11):
    print("%s * %s ="%(num,i),num*i)

#Write a Python Program to Print the Fibonacci sequence?
num=int(input("enter the number of terms: "))
a=0
b=1
if num<=0:
    print(" The requested series is: ",a)
else:
    print(" The requested series is: ", a,b)
    for i in range(2,num):
        b1=a+b
        print(b1,end=" ")
        a=b
        b=b1

#Write a Python Program to Check Armstrong Number?
Number = int(input("Please Enter the Number to Check: "))

Sum = 0
Times = 0

Temp = Number
while Temp > 0:
    Times = Times + 1
    Temp = Temp // 10

Temp = Number
while Temp > 0:
    Reminder = Temp % 10
    Sum = Sum + (Reminder ** Times)
    Temp //= 10

if Number == Sum:
           print("%d is Armstrong." %Number)
else:
           print("%d is Not." %Number)

 #Write a Python Program to Find Armstrong Number in an Interval?
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if num == sum:
            print(num)

#Write a Python Program to Find the Sum of Natural Numbers?
n=int(input("enter the number of terms to be considered: "))
sum=0
if n <0:
    print("Enter a positive number")
else:
    sum=0
    while n>0:
        sum+=n
        n=n-1
    print("The sum is",sum)


