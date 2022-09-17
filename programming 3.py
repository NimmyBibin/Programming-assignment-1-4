
#Write a Python Program to Check if a Number is Positive, Negative or Zero?
a=int(input("enter the number: "))
if a>0:
    print(" Given number is a positive number")
elif a<0:
    print("Given number  is a negative number")
else:
    print("the given number is zero")

#Write a Python Program to Check if a Number is Odd or Even?

a=int(input("enter the number: "))
if a%2==0:
    print("given number is an even number")
elif a%2!=0:
    print("given number is an odd number")
else:
    pass

#Write a Python Program to Check Leap Year?
#%100==0 is century year ,century year%4==0 is a leap year
year=int(input("enter the year: "))
if (year % 4 ==0) and (year % 100!=0):
    print(" %s is a leap year: " %year)
else:
    print("%s is not a leap year" %year)

#Write a Python Program to Check Prime Number?
num = int(input("enter the number: "))
if num > 1:
    for i in range(2, num//2):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
            break

#Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
for num in range(2, 10000):
        if num>1:
            for i in (2,num):
                if num%i==0:
                    break
                else:
                    print(num)
                    break




