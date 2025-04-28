class Employee:
    """Demonstrates Python's access modifiers (public, protected, private)."""
    
    def __init__(self, name: str, salary: float, ssn: str):
        self.name = name          # Public attribute (no underscore)
        self._salary = salary     # Protected attribute (single underscore)
        self.__ssn = ssn          # Private attribute (double underscore)

    def show_private(self) -> None:
        """Class method can access private members."""
        print(f"SSN (accessed internally): {self.__ssn}")

# Create employee
emp = Employee("John Doe", 75000.0, "123-45-6789")

# Accessing attributes:
print(f"Public name: {emp.name}")        # Works - public
print(f"Protected salary: {emp._salary}") # Works but shouldn't (protected)

try:
    print(f"Attempt to access private SSN: {emp.__ssn}")  # Will fail
except AttributeError as e:
    print(f"Access error: {e}")

# Proper way to access private member (via class method)
emp.show_private()

# Name mangling demonstration (how to actually access the private variable)
print(f"Name-mangled access: {emp._Employee__ssn}")  # Not recommended!
#NOTES:
#self.name: anyone can use it.
#self._salary: by convention, "please don’t touch this outside the class."
#self.__ssn: truly private — you can’t access it directly.