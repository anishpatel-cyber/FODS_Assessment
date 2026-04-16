'''
Program to create a class Learner and display
details of a learner.
'''

# Define class
class Learner:
    def __init__(self, roll_no, full_name, address, enrollment_year, program, group):
        self.roll_no = roll_no
        self.full_name = full_name
        self.address = address
        self.enrollment_year = enrollment_year
        self.program = program
        self.group = group

    # Method to display details
    def display_details(self):
        print("\nLearner Details:")
        print("Roll No:", self.roll_no)
        print("Name:", self.full_name)
        print("Address:", self.address)
        print("Year:", self.enrollment_year)
        print("Program:", self.program)
        print("Group:", self.group)

# Create object with user input
learner = Learner(
    input("Enter roll number: "),
    input("Enter full name: "),
    input("Enter address: "),
    input("Enter enrollment year: "),
    input("Enter program: "),
    input("Enter group: ")
)

# Display details
learner.display_details()