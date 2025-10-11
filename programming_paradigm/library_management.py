class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        """Add a book to the library"""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return True
        return False
    
    def return_book(self):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return True
        return False
    
    def list_available_books(self):
        """List all available books"""
        available_books = []
        for book in self._books:
            if not book._is_checked_out:
                available_books.append(book)
        return available_books
