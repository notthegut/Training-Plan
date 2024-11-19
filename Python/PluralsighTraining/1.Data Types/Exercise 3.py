#As seen with the previous examples, using things in python is similar to using them in JS, with print being used instead of console.log
#print(value to print)

#To convert something from a float to a integer we use int, for example
amount = int(10.6) 
print(amount)
#This will conver the 10.6 to the lowest integer avaliable, being 10

#To convert a integer to a float, use the float integer
amount = float(10)
print(amount)
#Here python appropiates the 10 to a decimel place


#Anything in a single quote is known as a string
name = 'Zain'
print(name)
#When we print this in the terminal only Zain will show

#Also works with double quotes
store_name = "Zain's store"
print(store_name)
#Makes sense to use double quotes as the string already has a single quote as an apostorphe, using a single string to wrap it will cause an error


#Can concatenate two strings using a plus sign
hello = "Hello"
name = "Zain"
greeting = hello + " " + name
print (greeting)

#You can make python ask for an input with a message to the user by using the input command as shown below
hello = "Hello"
my_name = input("What is your name")
greeting1 = hello + " " + my_name
print (greeting1)
#python will then ask for the user to input a value and then store this as the value
#The terminal will trigger for you to type in your name, in this you enter it


#If you want to make the user input trigger to look more neat, you can add a \n to the end of the input command which will trigger it to appear on the next line
hello = "Hello"
my_name = input("What is your name?\n")
greeting2 = hello + " " + my_name
print (greeting2)