# Program to calculate sum of positive and negative numbers

positive_sum = 0
negative_sum = 0

while True:

    num = int(input("Enter a number: "))

    # Check if number is positive
    if num > 0:
        positive_sum += num

    # Check if number is negative
    elif num < 0:
        negative_sum += num

    # Ask user if they want to continue
    choice = input("Do you want to continue? (yes/no): ")

    if choice == "no":
        break

# Display the results
print("Sum of positive numbers:", positive_sum)
print("Sum of negative numbers:", negative_sum)