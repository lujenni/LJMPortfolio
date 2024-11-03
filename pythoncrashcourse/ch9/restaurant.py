#Make a Class called Restaurant (9-1)
#Try it Yourself, pg 162

#Make a class called Restaurant
class Restaurant:
    """Labeling a restaurant's dish and open hours"""
    #The init method should have two attributes:
    #a restaurant_name and a cuisune)type
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attribute"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    #Make a method called describe_restaurat() that prints
    #the name and cuisine type
    def describe_restaurant(self):
        """Simulate restaurnt name and now serving food"""
        print(f"{self.restaurant_name}")
        print(f"Now serving {self.cuisine_type} !")
    #Make a method called open_restaurant() that prints a message
    #indicating the restaurant is open.
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

#Make an instance called restaurant from your class
restaurant = Restaurant('Olive Garden', 'alfredo')
time = Restaurant('Olive Garden', 'open')

#Print the two attributes indivdiually and then 
print(f"{restaurant.describe_restaurant}")
print(f"{time.open_restaurant}")

#call both methods with dot notation
restaurant.describe_restaurant()
time.open_restaurant()