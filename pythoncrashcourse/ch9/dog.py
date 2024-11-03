#Creating and using a class (OOP)
#Creating the dog class.

#define a Class called "dog"
class Dog:
    """A simple attempt to model a dog."""

    #a function that's part of a Class is a method
    #define the __init__ method to have three parameters
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

#Create an instance for a specific dog
my_dog = Dog('Willie', 6)
your_dog = Dog('Spencer', 9)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"My dog's name is {your_dog.name}.")
print(f"My dog is {your_dog.age} years old.")
your_dog.sit()