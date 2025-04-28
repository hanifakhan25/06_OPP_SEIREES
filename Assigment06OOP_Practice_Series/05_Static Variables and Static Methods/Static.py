class MathUtils:
    """A utility class containing mathematical operations."""
    
    @staticmethod
    def add(a: int|float, b: int|float) -> int|float:
        """Add two numbers and return the result.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b

# Using the static method
result = MathUtils.add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8
#NOTES:
#@staticmethod means: "This method doesn’t care about self or cls. Just does math."