expenses = [10.50,8,5,15,20,5,3]

sums = 0
#sum is what we are going to want to add each expense to as we loop through the list

for x in expenses:
    sums = sums + x

print("You spent $", sums, sep = "")
#This will automatically add everything from the expenses into the sum
#by adding the sep = "" part, we are telling python that everytime we want a space there has to "" present
#This allows there to not be a space between the dollar sign and the numbers

#Can also do this without using a list, by calling the sum function that is built into python
expense = [10.50,8,5,15,20,5,3]
total = sum(expense)
print("You spent $", total, sep = "")