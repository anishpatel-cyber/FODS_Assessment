#Program that takes two integers as parameters, Operate and return the result.

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def floor_div(a, b):
    return a // b

def power(a, b):
    return a ** b

#takes input from the user
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

#displays output
print("Addition:", add(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))
print("Floor Division:", floor_div(x, y))
print("Exponentiation:", power(x, y))