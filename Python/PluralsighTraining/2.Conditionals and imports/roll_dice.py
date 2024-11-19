#You can gain access and see all the different libraries and things as such on
# docs.python.org/3/library to see all the different libraries on offer

#To use any of the libraries we need to import them first
import random

#The function needed to gain a random variable between 2 values is random.randint(a.b)
roll = random.randint(1,6)

print("The computer has rolled a "+ str(roll))

#"Lets play a little game" (Jigsaw style yaara kussmeh)
#Incorporate it so that human input is used to guess what the dice number is

guess = int(input("Guess the dice roll:\n"))
if guess == roll:
    print("Correct! They rolled a "+ str(roll))
else:
    print("Wrong! They rolled a "+ str(roll))