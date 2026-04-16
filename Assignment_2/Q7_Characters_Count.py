#Program that takes a sentence as input and returns a dictionary
#showing how many times each character (excluding spaces) occurs

def key_value(sentence):
    result = {}

    for char in sentence:
        if char != " ":
            if char in result:
                result[char] += 1
            else:
                result[char] = 1

    return result

text = input("Enter a sentence: ")
print(key_value(text))