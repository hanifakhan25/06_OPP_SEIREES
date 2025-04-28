class Logger:
    def __init__(self, name):
        self.name = name
        print(f"{name}: Opened")
        
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name}: Closed")

# Usage:
with Logger("SafeLogger") as log:
    print("Doing work...")
#NOTES:
#  __init__ = when object is made.
#__del__ = when object is deleted.
#Great for debugging or cleanup.