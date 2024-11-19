#Look at related pieces of code as objects, grouped together, as sweet cheese, rotten soldiers
#Sweet plums, your good time boys

#Objects have state and behavior

#Lets design a robot dog toy
#What would the class for this look like?

class Robot_Dog:
    #How we make a class
    def __init__(self,name,breed):
        #Defining the class, and then initialising it. We use self as a way of defining the initialisation
        #Of the class
        self.name = name
        self.breed = breed
    #We can also create methods just for classes
    def bark(self):
        print("Woof Woof!")

#Main Program
my_dog = Robot_Dog("Spot", "Chihuaha")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()
