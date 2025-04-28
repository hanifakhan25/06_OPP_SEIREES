class Book:
    """A class representing books with a class-level counter."""
    
    total_books = 0  # Class variable to track all books created
    
    def __init__(self, title: str, author: str):
        """Initialize a book and increment the total count."""
        self.title = title
        self.author = author
        Book.increment_book_count()  # Call class method on instantiation

    @classmethod
    def increment_book_count(cls) -> None:
        """Increment the class-wide book counter."""
        cls.total_books += 1

    @classmethod
    def get_total_books(cls) -> int:
        """Return the total number of books created."""
        return cls.total_books

    @classmethod
    def reset_book_count(cls) -> None:
        """Reset the book counter (for testing purposes)."""
        cls.total_books = 0

# Demonstration
print(f"Initial book count: {Book.get_total_books()}")  # Output: 0

# Create some books
book1 = Book("Python Basics", "John Doe")
book2 = Book("Advanced Python", "Jane Smith")

# Check count
print(f"Total books after creation: {Book.get_total_books()}")  # Output: 2

# Reset count (for demonstration)
Book.reset_book_count()
print(f"Count after reset: {Book.get_total_books()}")  # Output: 0
#NOTES:
#Tracks how many books we’ve added.cls.total_books updates a shared counter for the whole class.