#working with classes and instances
#demonstrates modifying attributes' values through methods
#pg. 162, ch 9

class Car:
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    #define a method that puts a car's year, make, and model
    #into one string neatly describing the car
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    #create a new method to read the odometer
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
#outside of the class, we make an instance from teh Car class
#and assign it to a new variable (my_new_car)
#Then we call get_descriptive_name() to show what car we have
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
#Make an instance from the Car class
#then call read_odometer to show car mileage
my_new_car.update_odometer(23)
my_new_car.read_odometer()