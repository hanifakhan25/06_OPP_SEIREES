class A:
    """Base class in the diamond hierarchy."""
    
    def show(self):
        print("A")

class B(A):
    """First child class that overrides show()."""
    
    def show(self):
        print("B")
        super().show()  # Demonstrate MRO chaining

class C(A):
    """Second child class that overrides show()."""
    
    def show(self):
        print("C")
        super().show()  # Demonstrate MRO chaining

class D(B, C):
    """Diamond inheritance class combining B and C."""
    pass

# Create instance and demonstrate MRO
d = D()

print("Method Resolution Order (MRO):")
print(D.__mro__)  # Print
#NOTES:
#D inherits from both B and C. Python looks left to right → so B.show() is called.