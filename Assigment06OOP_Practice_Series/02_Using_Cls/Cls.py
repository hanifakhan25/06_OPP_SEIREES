class Counter:
    count = 0  # Class-level counter to track instances

    def __init__(self):
        """Increments the counter each time a new instance is created."""
        Counter.count += 1

    @classmethod
    def show_count(cls):
        """Displays the total number of Counter objects created."""
        print(f"Total objects created: {cls.count}")

# Testing the Counter
c1 = Counter()
c2 = Counter()
c3 = Counter()

Counter.show_count()  # Output: Total objects created: 3
#NOTES
#cls is like self, but for the whole class, not just one object.
#We’re using Counter.count to track how many times we made an object.
