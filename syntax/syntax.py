#how to print any statement
print("sonal")
#control statements
age=18
if age>18:
    print("sonal is eligible for voting")
else:
    print("sonal is not eligible for voting")


a=5
if a%2==0:
    print ('number is even')
else:
    print ('number is odd')
#how to import a file
import keyword
print("there are total",len(keyword.kwlist),"keywords in python")
print(keyword.kwlist)
#take input from user
print("enter two numbers")
a,b=input(),input()
c=a+b
print(c)
#type conversion
print("enter two numbers")
a,b=int(input()),int(input())
c=a+b
print("sum is :",c)
# if statement
x=-3
if x<0:
    print ("x is less than 0")
print("x is greater")
#program to check a number is positive or non positive using only if
a=int(input("enter a number:"))
if a>0:
    print("number is positive")
if a<=0:
    print("number is non positive")
#if-else statement
a=int(input("enter a number:"))
if a>0:
    print("number is positive")
else:
    print("number is non positive")
#if-elif-else
#write a program to print grade obtained in test.take marks obtained from user and display the grade.
marks=int(input("enter marks:"))
if 90<marks<=100:
    print("A")
elif 80<marks<=90:
    print("B")
elif 70<marks<=80:
    print("C")
elif 60<marks<=70:
    print("D")
elif 50<marks<=60:
    print("E")
else:
    print("F")

x=int(input("enter marks:"))
if x>90 :
    print("A")
elif x>80:
    print("B")
elif x>70:
    print("C")
elif x>60:
    print("D")
elif x>=50:
    print("E")
else:
    print("F")
#single line if else
#write a program to check whether a given number is even or odd.
a=int(input("enter a number:"))
print("even")if a%2==0 else print("odd")
#or
print("even" if int (input("enter a number"))%2==0 else "odd")