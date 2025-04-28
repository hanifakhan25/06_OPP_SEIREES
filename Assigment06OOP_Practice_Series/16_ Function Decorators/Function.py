from functools import wraps
from datetime import datetime

def log_function_call(func):
    """Decorator that logs function calls with timing information."""
    
    @wraps(func)  # Preserves original function metadata
    def wrapper(*args, **kwargs):
        # Log before call
        start_time = datetime.now()
        print(f"Calling {func.__name__} at {start_time:%H:%M:%S}")
        print(f"Arguments: {args if args else 'None'} | Keyword args: {kwargs if kwargs else 'None'}")
        
        # Execute function
        result = func(*args, **kwargs)
        
        # Log after call
        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        print(f"{func.__name__} returned {result} (execution time: {duration:.4f}s)")
        
        return result
    
    return wrapper

@log_function_call
def say_hello(name: str = "World") -> str:
    """Greet someone by name."""
    greeting = f"Hello, {name}!"
    print(greeting)
    return greeting

@log_function_call
def calculate_sum(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

# Demonstration
say_hello("Alice")
print()  # Spacer
calculate_sum(5, b=7) 
#NOTES:
#The decorator adds something before the function runs.
#Here, it prints a message before saying hello.