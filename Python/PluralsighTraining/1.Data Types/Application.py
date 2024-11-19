#Ask the user how old they are first and store it into a variable called age
#age = input("How old are you?\n")

#Then caluclate how many decades old they are by dividing the age by 10
#decades = age/10

#The above will give an error because it is trying to divide a string by a number, canny do that.
#You need to convert the input into a integer by wrapping it all with the integer function

#age = int(input("How old are you?\n"))
#decades = age/10
#print ("You are" + decades + "decades old.")

#The above will also give an error. When trying to concatenate strings in python, they all have to be a string, as decades is given as an integer we need to now
#convert it back into a string

#age = int(input("How old are you?\n"))
#decade = age/10
#print ("You are" + " " +  str(decade) + " " + "decades old.")


#This will give the decades as an decimal, for example 2.3.  If you want to change it to give you the decades and the years seperately
#Use integer division using //, and you can get the left over years that were not able to be divided using the modulus sign being %

age = int(input("How old are you?\n"))
decade = age // 10 # Directly divide by 10, giving you whole number results
year = age % 10 #Gives you the non-whole number results of the division
print ("You are" + " " + str(decade) + " " + "decades and" + " " + str(year) + " " + "year's old." )