# Program to find numbers divisible by 9 but not divisible by 6

start = int(input("Enter Starting Number: "))
end = int(input("Enter Ending Number: "))

for num in range(start,end+1):
    if num % 9 == 0 and num % 6 != 0:
        print(num)