# Book Class
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


# Library Class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book name: ")
        self.books.append(Book(title))
        print("Book added successfully.")

    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.available else "Borrowed"
            print(book.title, "-", status)

    def borrow_book(self):
        title = input("Enter book name to borrow: ")
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book borrowed successfully.")
                return
        print("Book not available.")

    def return_book(self):
        title = input("Enter book name to return: ")
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned successfully.")
                return
        print("Book not found.")


# Main Program
library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        library.borrow_book()

    elif choice == 4:
        library.return_book()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")


        
