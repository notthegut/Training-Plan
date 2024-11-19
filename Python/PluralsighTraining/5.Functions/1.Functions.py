#Functions are like mini programs within code
print ("hello world")
#used to print something to the console
name = input("Enter your name:\n")
#Input requires a user to input the data
amount = int(10.6)
#Int converts something to an integer
import random
roll = random.randint(1,6)
#randint used to give a random integer


#How do we define our own function

def greeting(name):
    print("Hello", name)
#When making your own function, we first
#Define it using def
#Put the name of the function after that
#Place the parameter for the function in brackets after that
#Function body indented underneath thisass

#Below it we will put the main program
input_name = input ("Enter your name:\n")
greeting(input_name)
#Ask user for their name
#Input the input of this into the function

#Need to define the function before you can call it



#A variable defined inside of a function can only be called within that function
#Known as local scope

#The variable name only exists within the function, and therefore if you tried to
#Print name it would show as undefined
#If a variable is made in the main program it has global scope and can therefore be used
#Anywhere within the main code of the program


def greetings():
    print("Eat my ass", name1)

name1 = input("What's your name?:\n")
greetings()  # Call the correct function

print(name1)

#Lets say you want to use a new name like name2, you have to reassing the original name to name2
name2 = "Abdul"
name1=name2
