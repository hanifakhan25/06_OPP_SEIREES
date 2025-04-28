class Multiplier:
    """A callable class that multiplies values by a fixed factor."""
    
    def __init__(self, factor: float):
        """Initialize with multiplication factor.
        
        Args:
            factor: The multiplication factor
        """
        if not isinstance(factor, (int, float)):
            raise TypeError("Factor must be a number")
        self.factor = float(factor)

    def __call__(self, x: float) -> float:
        """Multiply input by the stored factor.
        
        Args:
            x: The value to multiply
            
        Returns:
            The product of x and the stored factor
        """
        if not isinstance(x, (int, float)):
            raise TypeError("Input must be a number")
        return x * self.factor

    def __repr__(self) -> str:
        """Machine-readable representation."""
        return f"Multiplier(factor={self.factor})"

    def __str__(self) -> str:
        """Human-readable representation."""
        return f"Multiplier with factor {self.factor}"

# Demonstration
try:
    m = Multiplier("five")  # Will raise TypeError
except TypeError as e:
    print(f"Error: {e}")

m = Multiplier(5.0)
print(f"Is callable? {callable(m)}")  # True
print(f"5 × 10 = {m(10)}")          # 50.0
print(f"5 × 3.5 = {m(3.5)}")        # 17.5

try:
    print(m("text"))  # Will raise TypeError
except TypeError as e:
    print(f"Error: {e}")

# Show string representations
print(repr(m))  # Multiplier(factor=5.0)
print(str(m))   # Multiplier with factor 5.0

# Use case: Creating specialized multipliers
double = Multiplier(2)
triple = Multiplier(3)

numbers = [1, 2, 3]
print(f"Doubled: {[double(n) for n in numbers]}")  # [2, 4, 6]
print(f"Tripled: {[triple(n) for n in numbers]}")  # [3, 6, 9]
#NOTES:
#Now the object acts like a function!
#You can call it like m(10), and it'll multiply by the stored factor.