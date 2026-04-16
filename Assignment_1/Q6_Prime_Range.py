start = int(input("Enter Start: "))
end = int(input("Enter End: "))

count = 0
total = 0

for num in range(start, end+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num)
            count += 1
            total += num

print("Total Primes: " , count)
print("sum of Primes: " , total)