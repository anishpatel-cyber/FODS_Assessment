#Count how many times each number appears.

def count_frequency(lst):
    freq = {}

    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    return freq

# Taking input from user
numbers = list(map(int, input("Enter numbers: ").split()))

# Calling function
result = count_frequency(numbers)

print("Frequency:", result)