# Library Management System using OOP

class Book:
    def __init__(self, book_id, title, author):
        self.__book_id = book_id      # Private attribute (Encapsulation)
        self.__title = title
        self.__author = author
        self.__status = "Available"

    # Getter methods
    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_status(self):
        return self.__status

    # Issue book
    def issue_book(self):
        if self.__status == "Available":
            self.__status = "Issued"
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    # Return book
    def return_book(self):
        if self.__status == "Issued":
            self.__status = "Available"
            print("Book returned successfully.")
        else:
            print("Book is already available.")

    # Display book details
    def display(self):
        print("\nBook ID :", self.__book_id)
        print("Title   :", self.__title)
        print("Author  :", self.__author)
        print("Status  :", self.__status)


class Library:
    def __init__(self):
        self.books = []

    # Add a new book
    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully.")

    # View all books
    def view_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("\n----- Library Books -----")
            for book in self.books:
                book.display()

    # Search book by ID
    def search_book(self):
        book_id = input("Enter Book ID to search: ")

        for book in self.books:
            if book.get_book_id() == book_id:
                print("\nBook Found:")
                book.display()
                return

        print("Book not found.")

    # Issue book
    def issue_book(self):
        book_id = input("Enter Book ID to issue: ")

        for book in self.books:
            if book.get_book_id() == book_id:
                book.issue_book()
                return

        print("Book not found.")

    # Return book
    def return_book(self):
        book_id = input("Enter Book ID to return: ")

        for book in self.books:
            if book.get_book_id() == book_id:
                book.return_book()
                return

        print("Book not found.")

    # Delete book
    def delete_book(self):
        book_id = input("Enter Book ID to delete: ")

        for book in self.books:
            if book.get_book_id() == book_id:
                self.books.remove(book)
                print("Book deleted successfully.")
                return

        print("Book not found.")


# Main Program
library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        print("Thank you for using the Library Management System.")
        break

    else:
        print("Invalid choice. Please try again.")