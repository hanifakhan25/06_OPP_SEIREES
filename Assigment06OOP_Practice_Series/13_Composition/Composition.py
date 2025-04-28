class Engine:
    """A class representing a car engine."""
    
    def __init__(self, engine_type: str):
        """Initialize engine with a specific type."""
        self.engine_type = engine_type
        self.is_running = False

    def start(self) -> None:
        """Start the engine."""
        if not self.is_running:
            print(f"{self.engine_type} engine started")
            self.is_running = True
        else:
            print("Engine is already running")

    def stop(self) -> None:
        """Stop the engine."""
        if self.is_running:
            print("Engine stopped")
            self.is_running = False
        else:
            print("Engine is already stopped")

class Car:
    """A class representing a car composed with an engine."""
    
    def __init__(self, engine: Engine):
        """Initialize car with an engine."""
        self.engine = engine
        self.is_locked = True

    def start_car(self) -> None:
        """Start the car's engine."""
        if not self.is_locked:
            self.engine.start()
        else:
            print("Cannot start - car is locked")

    def unlock(self) -> None:
        """Unlock the car doors."""
        self.is_locked = False
        print("Car unlocked")

    def lock(self) -> None:
        """Lock the car doors."""
        self.is_locked = True
        print("Car locked")

# Usage
v8_engine = Engine("V8")
my_car = Car(v8_engine)

my_car.start_car()  # Output: Cannot start - car is locked
my_car.unlock()     # Output: Car unlocked
my_car.start_car()  # Output: V8 engine started
my_car.start_car()  # Output: Engine is already running
my_car.lock()       # Output: Car locked
#NOTES:
#The Car has an Engine. Car uses it like a part. That's composition.