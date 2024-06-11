class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

class Borrower:
    def __init__(self, borrower_id, name):
        self.borrower_id = borrower_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.transactions = []

    def add_book(self, book):
        self.books[book.book_id] = book

    def add_borrower(self, borrower):
        self.borrowers[borrower.borrower_id] = borrower

    def borrow_book(self, borrower_id, book_id):
        if borrower_id not in self.borrowers:
            print("Borrower not found")
            return
        if book_id not in self.books:
            print("Book not found")
            return
        book = self.books[book_id]
        if book.copies > 0:
            book.copies -= 1
            borrower = self.borrowers[borrower_id]
            borrower.borrowed_books.append(book)
            self.transactions.append((borrower_id, book_id))
        else:
            print("No copies available")

    def return_book(self, borrower_id, book_id):
        if borrower_id not in self.borrowers:
            print("Borrower not found")
            return
        if book_id not in self.books:
            print("Book not found")
            return
        borrower = self.borrowers[borrower_id]
        book = self.books[book_id]
        if book in borrower.borrowed_books:
            borrower.borrowed_books.remove(book)
            book.copies += 1
            self.transactions.append((borrower_id, book_id, 'returned'))
        else:
            print("Book not borrowed by this borrower")

    def get_borrower_info(self, borrower_id):
        if borrower_id not in self.borrowers:
            print("Borrower not found")
            return None
        borrower = self.borrowers[borrower_id]
        info = f"Borrower ID: {borrower.borrower_id}, Name: {borrower.name}, Borrowed Books: {[book.title for book in borrower.borrowed_books]}"
        return info

    def get_book_info(self, book_id):
        if book_id not in self.books:
            print("Book not found")
            return None
        book = self.books[book_id]
        info = f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Copies Available: {book.copies}"
        return info

#Testing 
library = Library()

#Adding books
library.add_book(Book(1, "1984", "George Orwell", 3))
library.add_book(Book(2, "To Kill a Mockingbird", "Harper Lee", 2))

#Adding borrowers
library.add_borrower(Borrower(101, "Alice"))
library.add_borrower(Borrower(102, "Bob"))

#Borrowing books
library.borrow_book(101, 1)
library.borrow_book(102, 1)
library.borrow_book(101, 3)
library.borrow_book(102, 2)

#Returning books
library.return_book(101, 1)
library.return_book(101, 2)

#Getting information
print(library.get_borrower_info(101))
print(library.get_book_info(1))
