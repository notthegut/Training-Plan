#You can have a list of lists brev madness ennih
menus = [ ["Egg Sandwich", "Bagel", "Covefe"],
         ["BLT", "PBJ", "Turkey Sandwich"],
         ["Soup", "Salad", "Spaghetti", "Taco"]]

#Can print each list by using their indicies
print("Breakfast Menu:\t", menus[0])
print("Lunch Menu:\t", menus[1])
print("Dinner Menu\t", menus[2])

#Lets say we wanna select Bagel from the first index, who we do it?
print(menus[0][1])
#Print the first number of list we want and the number of the item in that list

#what if we wanna change it to having a dictionary for each of the lists instead
menu = { "Breakfast" : ["Egg Sandwich", "Bagel", "Covefe"],
         "Lunch" : ["BLT", "PBJ", "Turkey Sandwich"],
         "Dinner" : ["Soup", "Salad", "Spaghetti", "Taco"]}

print("Breakfast Menu:\t", menu["Breakfast"])
print("Lunch Menu:\t", menu["Lunch"])
print("Dinner Menu\t", menu["Dinner"])

#Let see how we can use for loops and dictionaries to get the items we want

for item in menu:
    print(item)
    #This will print all the dictionaries in the list

#To get a specific value from a dictionary using a for loop, we need 2 variables, one for the dictionary and one for the
#Value

for name, menu in menu.items():
    print(name, ":", menu)

#Lets say we have a person and all their details are listed as key value pairs.
person = {"name" : "CallyManSam",
          "Age" : "34",
          "City" : "Blackpool"}

print(person.get("name"), person.get("Age"), person.get("City"))