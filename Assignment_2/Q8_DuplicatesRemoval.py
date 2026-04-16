#Program that accept a list of numbers from the user and return a new list with
#all duplicates removed and the numbers sorted in ascending order

nums = list(map(int, input("Enter numbers: ").split()))

unique = list(set(nums))
unique.sort()

print("Result:", unique)