# computer_choice = "scissors"
# user_choice = input("Do you want rock,paper or scissors\n")

# if computer_choice == user_choice:
#     print("TIE")
# elif user_choice =="rock" and computer_choice == "scissors":
#     print("WIN)")
# elif user_choice =="paper" and computer_choice == "rock":
#     print("WIN)")
# elif user_choice =="scissors" and computer_choice == "paper":
#     print("WIN)")
# else:
#     print("LOSE")

#Can incorportate the random sequences fucntion. In this, you provide python with a sequence of numbers
#and python will chose one from it at random. incorporate this into the RPS game to allow for it to chose one
#number at random and have it be applied to one of the choices
import random
#First import the random functions
computer_choice= random.choice(["rock", "paper", "scissors"])
#Here the computer will then chose out of rock paper and scissors, provided in a list given above
user_choice = input("Do you want rock,paper or scissors\n")

print("Computer choice", computer_choice)

if computer_choice == user_choice:
    print("TIE")
elif user_choice =="rock" and computer_choice == "scissors":
    print("WIN")
elif user_choice =="paper" and computer_choice == "rock":
    print("WIN")
elif user_choice =="scissors" and computer_choice == "paper":
    print("WIN")
else:
    print("LOSE")