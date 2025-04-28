class Product:
    """A product with price management using property decorators."""
    
    def __init__(self, price: float):
        """Initialize with price validation."""
        self._price = None  # Initialize first
        self.price = price  # Use property setter for validation

    @property
    def price(self) -> float:
        """Get the product price.
        
        Returns:
            The current price of the product
        """
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Set the product price with validation.
        
        Args:
            value: New price value (must be positive)
            
        Raises:
            ValueError: If price is negative
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Price must be a number")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = float(value)  # Ensure float storage

    @price.deleter
    def price(self) -> None:
        """Delete the price and log this action."""
        print(f"Deleting price (was {self._price})")
        del self._price

    def apply_discount(self, percentage: float) -> None:
        """Apply a discount to the price.
        
        Args:
            percentage: Discount percentage (0-100)
        """
        if not 0 <= percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        self.price *= (100 - percentage) / 100  # Uses property setter

# Demonstration
try:
    item = Product(-50)  # Will raise ValueError
except ValueError as e:
    print(f"Error: {e}")

item = Product(100.0)
print(f"Initial price: ${item.price:.2f}")  # $100.00

item.price = 150.49  # Valid assignment
print(f"Updated price: ${item.price:.2f}")  # $150.49

item.apply_discount(20)  # 20% discount
print(f"After discount: ${item.price:.2f}")  # $120.39

del item.price  # Output: Deleting price (was 120.392)
try:
    print(item.price)  # Will raise AttributeError
except AttributeError:
    print("Price attribute was successfully deleted")
    
#NOTES:
# This lets you treat methods like variables.
#You can get, set, or delete like you're using a normal variable.