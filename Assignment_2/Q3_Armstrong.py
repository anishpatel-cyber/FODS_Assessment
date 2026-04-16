#Program that accepts a string as input and checks whether it is armstrong or not

def armstrong(num):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10

    return total == num

num = int(input("Enter number: "))

if armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")