class Car:
    """A simple class representing a car with a brand and start functionality."""
    
    def __init__(self, brand: str):
        """Initialize the car with a brand name."""
        self.brand = brand  # Public variable (default in Python)

    def start(self) -> None:
        """Simulate starting the car."""
        print(f"{self.brand} car is starting...")

# Create and use the car object
my_car = Car("Toyota")
print(f"Car brand: {my_car.brand}")  # Access public variable
my_car.start()  # Call public method
#NOTES:
#Everything here is public. We can access brand and call start() from outside the class freely.
