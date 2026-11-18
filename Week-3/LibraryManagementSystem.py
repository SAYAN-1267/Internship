class Library:
    def __init__(self):
        self.books = []

    # Add a book
    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(book, "added successfully")
        else:
            print("Book already exists")

    # Remove a book
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "removed successfully")
        else:
            print("Book not found")

    # Issue a book
    def issue_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(book, "issued successfully")
        else:
            print("Book is not available")

    # Return a book
    def return_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(book, "returned successfully")
        else:
            print("Book is already available")

    # Display available books
    def display_books(self):
        print("Available Books:", self.books)


# Creating object
library = Library()

library.add_book("Python")
library.add_book("Java")
library.add_book("C++")

library.display_books()

library.issue_book("Python")
library.display_books()

library.return_book("Python")
library.display_books()

library.remove_book("Java")
library.display_books()