# __repr__ AND __str__
import datetime
today = datetime.datetime.now()

# Prints readable format for date-time object
# Used for creating user-friendly output and for displaying the object as a string
print(str(today))

# prints the official format of date-time object
# Used for debugging and development purposes to get the complete information of an object
print(repr(today))

#ANOTHER EXAMPLE
class Animal:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"This is a pet named {self.name}"
    
    def __repr__(self):
        return f"Animal(name='{self.name}')"


pet = Animal("dog")
print(repr(pet))               
print(str(pet))
print(pet)                       #Internally uses str(obj) (falls back to repr(obj) if __str__ isn’t defined)
