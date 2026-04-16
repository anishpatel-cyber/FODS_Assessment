'''
Program to read a CSV file named "records.csv"
and display its contents.
'''

# open file in read mode
file = open("records.csv", "r")

# read all content
data = file.read()

# Display the content
print("File Contents:\n")
print(data)

file.close()    