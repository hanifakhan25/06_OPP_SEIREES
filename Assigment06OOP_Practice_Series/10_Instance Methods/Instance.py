class Dog:
    """A class representing a dog with name and breed attributes."""
    
    def __init__(self, name: str, breed: str):
        """Initialize dog with name and breed.
        
        Args:
            name: The dog's name
            breed: The dog's breed
        """
        self.name = name
        self.breed = breed

    def bark(self, times: int = 1) -> None:
        """Make the dog bark.
        
        Args:
            times: Number of barks (default: 1)
        """
        for _ in range(times):
            print(f"{self.name} the {self.breed} says: Woof!")

    def describe(self) -> None:
        """Print a description of the dog."""
        print(f"{self.name} is a {self.breed}")

# Create and use a Dog instance
my_dog = Dog("Buddy", "Labrador")
my_dog.describe()  # Output: Buddy is a Labrador
my_dog.bark(3)     # Output: Buddy the Labrador says: Woof! (3 times)

#NOTES:
#bark() uses self.name to know which dog is barking. Each dog barks with its name.