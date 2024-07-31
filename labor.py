from numba import jitclass, int32

# Define the class with the jitclass decorator
@jitclass
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

# Create an instance of the compiled class
my_instance = MyClass(10, 20)

# Call the add method on the instance
result = my_instance.add()

print(result)  # Output: 30
