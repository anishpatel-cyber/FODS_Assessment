'''
Program to copy contents from one file to another
Use try/except to handle exceptions.
'''

try:
    # Step 1: Take file names from user
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")

    # Step 2: Open source file
    with open(source, "r") as f1:
        data = f1.read()

    # Step 3: Create new file (x mode prevents overwrite)
    with open(destination, "x") as f2:
        f2.write(data)

    print("File copied successfully!")

# If source file not found
except FileNotFoundError:
    print("Error: Source file does not exist")

# If destination file already exists
except FileExistsError:
    print("Error: Destination file already exists")