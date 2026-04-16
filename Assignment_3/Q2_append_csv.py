'''
Program to take user details as input and append them
to an existing CSV file named "records.csv".
'''

# Open file in append mode
file = open("records.csv", "a")

# Take user input
student_name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
program = input("Enter program: ")
year = input("Enter year: ")
group = input("Enter group: ")

# Write data into file in CSV format
file.write(f"{student_name},{roll_no},{program},{year},{group}\n")

print("Data added successfully!")

# Close the file
file.close()