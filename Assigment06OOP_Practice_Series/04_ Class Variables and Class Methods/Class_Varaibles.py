class Bank:
    """A class representing a bank with a shared name across all instances."""
    
    bank_name = "ABC Bank"  # Class variable (shared by all instances)

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        """Class method to update the bank name for all instances."""
        cls.bank_name = new_name

# Create instances
b1 = Bank()
b2 = Bank()

# Before changing the name
print(f"Original bank name (via class): {Bank.bank_name}")  # Output: ABC Bank

# Change the name using the class method
Bank.change_bank_name("XYZ Bank")

# After changing the name
print(f"b1's bank name: {b1.bank_name}")  # Output: XYZ Bank
print(f"b2's bank name: {b2.bank_name}")  # Output: XYZ Bank
#NOTES:
#bank_name is shared by all objects.
#Change it once, and all banks see the new name.