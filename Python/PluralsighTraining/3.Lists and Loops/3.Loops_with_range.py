#So using the expenses example, lets say we want to have it so a user can add their own expesnes instead of using
#the hard coded expenses given previously

#We can use the range() function for this

range(7) #this will give numbers from 0,1,2,3,4,5,6
#We can customise it by giving it a start, stop and step value
range(0,7,1) #0 being the start, 7 being the stop and 1 being the step or the incriment each loop

#So what does the syntax look like for this typa loop?
for i in range(7):
    print(i)






#We can therefore then add this loop into the previous example and ask the user to input say 7 expenses
#using the for loop and have it push them into a list

# total = 0
# expenses = []
# for i in range(7):
#     expenses.append(float(input("Enter an expense")))
# #Here we have expenses.append(float(input("Enter an expense")))
# #expenses.append - used to add the input to the end of the list
# #float - used to convert the value given into a float so it can be used.we use float instead of int as we can have a 
# #non whole value expense
# #input - used to ask the user for an actual input to be given and used
# total = sum(expenses)

# print("You have spent $", total , sep = "")

#Lets say you want to ask the user for the number of expenses and use that instead of giving a set value of expenses
total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:\n"))
#here we are using
#int - since the number of expenses can only be a whole number
#input - used to trigger the number of expenses from the customer, this will allow for python to then store the
#number of expenses in the variable num_expenses

for i in range(num_expenses):
    expenses.append(float(input("Enter an expense\n")))

total = sum(expenses)
print("You spent $", total, sep = "")