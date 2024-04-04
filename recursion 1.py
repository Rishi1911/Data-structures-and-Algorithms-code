#print N natural number
def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=" ")
printN(10)
print("\n")
#natural number in reverse order
def f(n):
    if n>0:
        print(n,end=" ")
        f(n-1)
    else:
        return
f(10)
print("\n")
#N natural odd numbers
def f1(n):
    if n>0:
        f1(n-1)
        print(2*n-1,end=" ")
f1(10)
print("\n")
#N natural even number
def f1(n):
    if n>0:
        f1(n-1)
        print(2*n,end=" ")
f1(5)
print("\n")
# N reverse odd number
def f(n):
    if n>0:
        print(2*n-1,end = " ")
        f(n-1)
f(5)
print("\n")
#N reverse even number
def f(n):
    if n>0:
        print(2*n,end=" ")
        f(n-1)
f(10)
print("\n")
# to calculate the sum of N natural Number
def f(n):
    if n==1 :
        return 1
    return n + f(n-1)
p = f(5)
print(p)
#sum of odd number
def f(n):
    if n==1:
        return 1
    return 2*n-1 + f(n-1)
z = f(5)
print(z)
# sum of even number
def f(n):
    if n==1:
        return 2
    return 2*n + f(n-1)
z = f(5)
print(z)
#factorial of number
def f(n):
    if n==1:
        return 1
    return n*f(n-1)
z = f(5)
print(z)
# sum of squares of N natural numbers
def f(n):
    if n == 1:
        return 1
    return n*n + f(n-1)
z = f(5)
print(z)
