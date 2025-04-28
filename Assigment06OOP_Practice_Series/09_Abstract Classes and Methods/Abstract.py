from abc import ABC, abstractmethod
from typing import Union

class Shape(ABC):
    """Abstract base class representing a geometric shape."""
    
    @abstractmethod
    def area(self) -> Union[float, int]:
        """Calculate and return the area of the shape.
        
        Returns:
            float or int: The calculated area of the shape
        """
        pass

class Rectangle(Shape):
    """Concrete class representing a rectangle, inheriting from Shape."""
    
    def __init__(self, length: Union[float, int], width: Union[float, int]):
        """Initialize rectangle with length and width.
        
        Args:
            length: The length of the rectangle
            width: The width of the rectangle
        """
        self.length = length
        self.width = width

    def area(self) -> Union[float, int]:
        """Calculate rectangle area (length × width)."""
        return self.length * self.width

# Usage
try:
    shape = Shape()  # This will raise an error - can't instantiate abstract class
except TypeError as e:
    print(f"Error: {e}")  # Expected output: Can't instantiate abstract class Shape with abstract method area

rectangle = Rectangle(5.5, 3)
print(f"Rectangle area: {rectangle.area()}")  # Output: Rectangle area: 16.5
#NOTES
#You can’t make a Shape directly.
#It's a blueprint for shapes. Rectangle must fill in the area() met