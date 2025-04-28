from typing import Any

def add_greeting_method(cls: Any) -> Any:
    """Class decorator that adds a greet method to classes.
    
    Args:
        cls: The class being decorated
        
    Returns:
        The modified class with new greet method
    """
    def greet(self) -> str:
        """Greet with both the decorator message and instance name."""
        return f"Hello from Decorator! My name is {self.name}."
    
    # Add the method to the class
    cls.greet = greet
    
    # Add a class-level attribute
    cls.decorator_added = True
    
    return cls

@add_greeting_method
class Person:
    """A simple person class that will be enhanced by the decorator."""
    
    def __init__(self, name: str):
        """Initialize with a name."""
        self.name = name

    def original_greet(self) -> str:
        """Original greeting method."""
        return f"Hi, I'm {self.name}."

# Demonstration
p = Person("Ali")

# Using the decorated method
print(p.greet())          # Output: Hello from Decorator! My name is Ali.

# Original method still works
print(p.original_greet()) # Output: Hi, I'm Ali.

# Class-level attribute added by decorator
print(f"Was decorated? {Person.decorator_added}")  # Output: Was decorated? True

# Show all methods/attributes
print("\nAvailable methods/attributes:")
print(dir(p))
#NOTES:
# The class decorator adds a new method to the class after it's created.
#Now Person().greet() returns a custom message.