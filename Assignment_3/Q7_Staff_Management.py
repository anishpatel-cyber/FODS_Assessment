'''
Program to create a class Staff and store multiple staff details
in a CSV file (staff.csv). The program also allows the user to
view staff records. Exception handling is used.
'''

# Define Staff class
class Staff:
    def __init__(self, emp_id, full_name, address, phone_number, marital_status, dependents, salary):
        self.emp_id = emp_id
        self.full_name = full_name
        self.address = address
        self.phone_number = phone_number
        self.marital_status = marital_status
        self.dependents = dependents
        self.salary = salary


try:
    while True:
        print("\n--- Staff Management System ---")
        print("1. Add Staff")
        print("2. View Staff")
        print("3. Exit")

        choice = input("Enter your choice: ")

        # OPTION 1: Add Staff
        if choice == "1":
            n = int(input("Enter number of staff members: "))

            # Using 'with open' ensures file is saved properly
            with open("staff.csv", "a") as file:

                for i in range(n):
                    print(f"\nEnter details for staff {i+1}")

                    emp_id = input("Employee ID: ")
                    full_name = input("Full Name: ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    marital_status = input("Marital Status: ")
                    dependents = input("Number of Dependents: ")
                    salary = input("Salary: ")

                    # Create Staff object
                    staff = Staff(emp_id, full_name, address, phone_number, marital_status, dependents, salary)

                    # Write data into CSV file
                    file.write(f"{staff.emp_id},{staff.full_name},{staff.address},{staff.phone_number},{staff.marital_status},{staff.dependents},{staff.salary}\n")

            print("Staff data saved successfully!")

        # OPTION 2: View Staff
        elif choice == "2":
            try:
                with open("staff.csv", "r") as file:
                    print("\n--- Staff Records ---\n")
                    data = file.read()

                    if data == "":
                        print("No records found.")
                    else:
                        print(data)

            except FileNotFoundError:
                print("No file found. Please add staff first.")

        # OPTION 3: Exit
        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")

# Exception handling
except ValueError:
    print("Invalid input! Please enter correct values.")

except Exception as e:
    print("Unexpected error:", e)