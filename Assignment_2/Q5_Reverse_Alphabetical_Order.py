#Program that accepts a list of names and returns the names in reverse aplhabetical order.

def reverse_sort(names):
    return sorted(names, reverse=True)

names = ["Anish", "Satya", "Binit", "Nitesh"]
print(reverse_sort(names))