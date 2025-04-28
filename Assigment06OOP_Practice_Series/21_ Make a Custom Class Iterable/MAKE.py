class Countdown:
    """A custom iterable that counts down from start to 0.
    
    Features:
    - Counts down from any positive integer
    - Implements full iterator protocol
    - Supports reverse iteration
    - Includes length and representation
    """
    
    def __init__(self, start: int):
        """Initialize the countdown.
        
        Args:
            start: Positive integer to start counting down from
            
        Raises:
            ValueError: If start is not a positive integer
        """
        if not isinstance(start, int) or start < 0:
            raise ValueError("Start must be a positive integer")
        self.start = start
        self.current = start

    def __iter__(self):
        """Reset and return the iterator."""
        self.current = self.start
        return self

    def __next__(self) -> int:
        """Get the next countdown value.
        
        Returns:
            The next integer in countdown sequence
            
        Raises:
            StopIteration: When countdown reaches below 0
        """
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

    def __reversed__(self):
        """Return a generator counting up from 0 to start."""
        return (i for i in range(self.start + 1))

    def __len__(self) -> int:
        """Return the length (start + 1)."""
        return self.start + 1

    def __repr__(self) -> str:
        """Return official string representation."""
        return f"Countdown(start={self.start})"

# Demonstration
try:
    # Test invalid initialization
    cd = Countdown(-5)
except ValueError as e:
    print(f"Error: {e}")

print("\nCountdown from 5:")
cd = Countdown(5)
for num in cd:
    print(num, end=" ")  # Output: 5 4 3 2 1 0

print("\n\nCountdown features:")
print(f"Length: {len(cd)}")          # Output: 6
print(f"Representation: {cd!r}")     # Output: Countdown(start=5)

print("\nReverse countup:")
for num in reversed(cd):
    print(num, end=" ")  # Output: 0 1 2 3 4 5

print("\n\nMultiple iterations:")
# Works because __iter__ resets self.current
for num in cd:
    print(num, end=" ")  # Output: 5 4 3 2 1 0
print()
for num in cd:
    print(num, end=" ")  # Output: 5 4 3 2 1 0
#NOTES:
#You made your own loop!
#It counts down, and Python knows when to stop using StopIteration.