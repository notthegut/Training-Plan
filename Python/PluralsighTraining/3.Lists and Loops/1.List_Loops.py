#A list is a container that can store anything we want
empty = []
words = ['Lol', 'IDK']
nums = [5,10,15]
mixed = [5, 'SDK', 1.5]

#Can even have a list of lists
lists = [['A','B','C'], ['D','E','F']]

#An items index is it position in a list
#Order starts as shown below
#0,1,2,3 - First index for the first object is a 0 and it increases upwards from that point onwards
inches = [5.5,6.4,7.8]
print (inches[0]) #This will give the first item in the list
print (inches[2]) #Will give the 3rd item in the list

#To find the nth number in a list you would use n-1 

#Creating a list requires square brackets
acronyms = []
#Here we have an empty list, denoted by the square brackets with nothing inside it
acronyms.append('LOL')
acronyms.append('IDK')
#Then we add things to the list by using append
print(acronyms)

#You can also add items to the end of an already existing list using the same methedology
acronym = ['LOL','IDK', 'SMH']
acronym.append('BFN')
acronym.append('IMHO')
print(acronym)

#This is known as calling a method, where acronyms is what we want to edit, append is the method, and whatever
#is in the brackets is what we want to either add or remove 

#To remove an item we use the remove method and pass in the value we want to remove
acronym.remove('BFN')
print(acronym)

#Can also remove an item based upon its index in the list by using del and the formatting seen below.
del acronym[2]
print(acronym)



#How to check if an item exists in a list, we can use a if statement
if 1 in [1,2,3,4,5]:
    print("its there")


#So see below
active = ['LOL', 'IDK', 'SMH', 'TBH']
word = 'BFN'

if word in active:
    print(word + ' is in the list')
else:
    print(word + ' is NOT in the list')

#When you print a list it will print it in the exact same way as it was written
print(active)
#To make it print out the whole list we would need to use a for loop
for acco in active:
    print(acco)
#Here acco is used as a temporary variable that will hold one of the acronyms in the list for each run
#Essentially we are telling python to list each acco being equivalent to one variable in active
#For each time it goes through the loop, capiche?