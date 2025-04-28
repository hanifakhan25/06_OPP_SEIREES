class Student:
    def __init__(self, name: str, marks: float):
        self.name = name      # 'self.name' means this object's name
        self.marks = marks    # 'self.marks' means this object's marks

    def display(self) -> None:
        print(f"Student Name: {self.name}")
        print(f"Marks Obtained: {self.marks}/100")
        if self.marks >= 40:
            print("Status: Passed")
        else:
            print("Status: Failed")

# Creating a student object
s1 = Student("Ali", 87)

# Displaying student info
s1.display()
#NOTES:
#class Student: → Think of this as a blueprint for making students.

#__init__() → It's a special method that runs when you make an object.

#self → It means "this object". It helps each student object keep its own data.

#display() → A simple function that prints stuff.