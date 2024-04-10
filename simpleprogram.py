''' 
3. Write a Program to add two numbers User through.
4. Write a Program to subtract two numbers User through.
5. Write a Program to multiplication of two numbers User through.
6. Write a Program to division of two numbers User through.
7. Write a Program to modulus of two numbers User through.

10.Write a Program to find area of circle and perimeters. 

11. Write a Program to calculate Simple Interest.
12. Write a Program to calculate Compound Interest. 

13. Write a Program to convert meter into centimeter.

15. Write a Program to enter divisor and dividend find quotient and reminder.

16. Write a Program to swap two numbers using two variables.
17. Write a Program to swap two numbers using third variables. 

18. Write a Program to convert Celsius into Fahrenheit.
19.Write a Program to convert Fahrenheit into Celsius.

21. Write a Program to find greater number among two number using ternary operator'''

a = int(input("enter the number"))
b = int(input("enter the number"))
print(a-b)
print(a+b)
print(a*b)
print(a/b)
print(a%b)

print("area of circle",3.14*a*a)

print("perimeterof circle", round(2*3.14*a,2))

t = int(input("time"))
a = int(input("amount"))
i = int(input("intrest"))
print(t*a*i)

print(a*(1+i)**t)

x = int(input("Enter the value of meter"))
print("the value of centimeter is", x*100)

divisor =  int(input("Enter the divisor"))
dividend = int(input("Enter the dividend"))
remainder = divisor % dividend
quotient = divisor /  dividend
print(remainder,quotient)

a = 10
b = 20
a = a+b
b= a-b
a=a-b
print(a,b)

a = 10
b = 20
temp = a
a = b
b = temp
print(a,b)

c = int(input("enter the celsuis"))
f = (c * 9/5)+32
print(f)
f = int(input("enter the farhenite"))
c = (f - 32) * 5/9
print(c)

a = int(input("enter the number"))
b = int(input("enter the number"))
c = a if a > b else b
print(c)







