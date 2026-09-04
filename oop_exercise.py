class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False

        if self.year < 0:
            raise ValueError("Year cannot be negative")

    def check_out(self):
        """Mark the book as checked out."""
        if self.checked_out:
            raise ValueError(f"The book '{self.title}' is already checked out.")
        self.checked_out = True

    def return_book(self):
        """Mark the book as returned."""
        if not self.checked_out:
            raise ValueError(f"The book '{self.title}' is not checked out.")
        self.checked_out = False

    def __repr__(self):
        status = 'Checked Out' if self.checked_out else 'Available'
        return f"'{self.title}' by {self.author} ({self.year}) - {status}"

class Ebook(Book):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def __repr__(self):
        status = 'Checked Out' if self.checked_out else 'Available'
        return f"'{self.title}' by {self.author} ({self.year}) - {status}, File Size: {self.file_size_mb}MB"

    counter = 0  # Class variable to keep track of the number of Ebook instances

    def check_out(self):
        """Mark the ebook as checked out and increment the counter."""
        super().check_out()
        Ebook.counter += 1

class Catalog:
    """Manages a collection of books."""

    def __init__(self):
        self.books = []  # Internal list of book objects

    def add_book(self, book):
        """Add a new book to the catalog."""
        if not isinstance(book, Book):
            raise ValueError("Only instances of Book or its subclasses can be added.")
        self.books.append(book)

    def get_available_books(self):
        """Return all available books."""
        return [book for book in self.books if not book.checked_out]

    def summary(self):
        """Return a summary of all books."""
        total = len(self.books)
        checked_out = sum(1 for book in self.books if book.checked_out)
        print(f"\nCatalog Summary: {checked_out}/{total} checked out.")
        for book in self.books:
            print(f" - {book}")

    def search_by_title(self, title):
        """Search for books by title."""
        return [book for book in self.books if title.lower() in book.title.lower()]

catalog = Catalog()
catalog.add_book(Book("Python Crash Course", "Eric Matthes", 2019))
catalog.add_book(Book("Clean Code", "Robert Martin", 2008))
catalog.add_book(Ebook("AI Engineering", "Chip Huyen", 2025, 15.2))

# Search
results = catalog.search_by_title("python")
print(results)  # Should find "Python Crash Course"

# Check out
catalog.books[0].check_out()
available = catalog.get_available_books()
print(f"Available: {len(available)} books")

catalog.summary()