# This is an example of object oriented programming

# We are basically creating our own datatype entitled "Animal"
class Animal:
    # __init__() is a base function that exists in Python Standard Library
    # We are "overriding" the behaviour of it so that our own class can have its own "initialization method"

    # Our Animal class when initialized (when a variable is type Animal), it must be given an argument for the name attribute
    # Example --> example = Animal("Jerry") ... example.name now has "Jerry"
    # self is a keyword reserved for classes to help them reference their own attributes and methods 
    def __init__(self, name):
        self.name = name
        self.__creator = "Mr. Park" # this is an example of an encapsulated attribute; the attribute has a double underscore
                                    # in front; and it is not accessible outside of the class definition

    # sound(noise) is an example of a method. The Animal class has a method that prints the given noise argument
    def sound(self, noise):
        print(noise)
    
    # This is to show that we can still access encapsulated values within the class definition
    def get_creator(self):
        print(f"{self.name} is created by {self.__creator}.")

# Dog class is an child/inherited class of Animal
# It will have all the attributes and methods that Animal has
class Dog(Animal):
    
    # Dog has its own custom class, but it uses its own sound() method to bark
    def bark(self):
        self.sound("bark bark!")

d = Dog("Marshall")
d.bark()
d.get_creator() # no error; we are accessing Dog's Parent method called get_creator()
print(d.name) # printing dog's name
print(d.__creator) # will create error; the creator attribute is encapsulated, so we cannot access it from outside.