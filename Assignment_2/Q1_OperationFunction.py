#Program that takes two integers as input and displays output..

def operations(a, b):
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Quotient:", a / b)

# Input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

operations(x, y)