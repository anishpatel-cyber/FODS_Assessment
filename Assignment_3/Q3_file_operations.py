'''
Program to take two numbers from the user, perform
basic arithmetic operations, and store the results
in a file along with date and time.
'''

import datetime

file = open("result.txt", "a")

while True:
    #Taking input from the user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    #write results to file
    file.write(f"\nDate: {datetime.datetime.now()}\n")
    file.write(f"Addition: {a+b}\n")
    file.write(f"Subtraction: {a-b}\n")
    file.write(f"Multiplication: {a*b}\n")
    file.write(f"Division: {a/b}\n")

    choice = input("Continue? (yes/no): ")

    if choice == "no":
        break

file.close()

# display file content
file = open("result.txt", "r")
print(file.read())
file.close()