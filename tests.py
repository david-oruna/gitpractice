a = ["apple", "banana"]

print("c" in a)

class Dog:
 
    # class attribute
    attr1 = "mammal"
 
    # Instance attribute
    def __init__(self, name):
        self.name = name
 
# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")
 
# Accessing class attributes
print(f"Rodger is a {Rodger.__class__.attr1}")
print(f"Tommy is also a {Rodger.__class__.attr1}")
 
# Accessing instance attributes
print(f"My name is {Rodger.name}")
print(f"My name is {Tommy.name}")