'''
Program to create a simple Library Management System
using class. It allows user to search, borrow and return books.
'''

# Define Library class
class Library:
    def __init__(self):
        # Initial list of books
        self.books = ["Python", "Math", "Science", "English", "C++", "Networking",
        "MultiMedia"]

    # Method to display all books
    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            print("-", book)

    # Method to search book
    def search_book(self, book_name):
        if book_name in self.books:
            print("Book is available")
        else:
            print("Book not found")

    # Method to borrow book
    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print("Book borrowed successfully")
        else:
            print("Book not available")

    # Method to return book
    def return_book(self, book_name):
        self.books.append(book_name)
        print("Book returned successfully")


# Create Library object
library = Library()

# Menu-driven program
while True:
    print("\n--- Library Menu ---")
    print("1. Display Books")
    print("2. Search Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.display_books()

    elif choice == "2":
        book = input("Enter book name to search: ")
        library.search_book(book)

    elif choice == "3":
        book = input("Enter book name to borrow: ")
        library.borrow_book(book)

    elif choice == "4":
        book = input("Enter book name to return: ")
        library.return_book(book)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")