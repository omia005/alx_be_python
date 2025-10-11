class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def __str__(self):
        status = "checked out" if self._is_checked_out else "available"
        return f"'{self.title}' by {self.author} - {status}"

class Library:
    def __init__(self):
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a book to the library"""
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only Book objects can be added to the library")
    
    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title.lower() == title.lower() and not book._is_checked_out:
                book._is_checked_out = True
                print(f"Successfully checked out: '{book.title}'")
                return
        print(f"Book '{title}' not found or already checked out")
    
    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title.lower() == title.lower() and book._is_checked_out:
                book._is_checked_out = False
                print(f"Successfully returned: '{book.title}'")
                return
        print(f"Book '{title}' not found or not checked out")
    
    def list_available_books(self):
        """List all available books"""
        available_books = [book for book in self._books if not book._is_checked_out]
        
        if not available_books:
            print("No available books in the library")
        else:
            print("Available books:")
            for book in available_books:
                print(f"  - '{book.title}' by {book.author}")
