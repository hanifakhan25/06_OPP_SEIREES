class Person:
    """Base class representing a person."""
    
    def __init__(self, name: str):
        """Initialize person with name."""
        self.name = name

class Teacher(Person):
    """Derived class representing a teacher, inheriting from Person."""
    
    def __init__(self, name: str, subject: str):
        """
        Initialize teacher with name and subject.
        Uses super() to call parent class's __init__.
        """
        super().__init__(name)  # Initialize the Person part
        self.subject = subject  # Add Teacher-specific attribute

# Create and use a Teacher instance
teacher = Teacher("Ms. Sara", "Mathematics")
print(f"Teacher: {teacher.name}, Subject: {teacher.subject}")
#NOTES:
#🧠 super() means: "call the parent’s method."
#Used here to call the Person constructor when creating a Teacher.