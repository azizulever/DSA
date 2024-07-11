# calculating factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

n = int(input("enter number "))
print(factorial(n))


# fibonacci series
def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("enter number "))
print(fibonacci(n))


# sum of all numbers
def sum(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return n + sum(n-1)
    
n = int(input("enter number "))
print(sum(n))
