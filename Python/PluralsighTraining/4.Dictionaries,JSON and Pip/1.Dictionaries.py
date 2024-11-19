#A way of maintianing two lists
acronym = ["LOL", "IDK", "TBH"]
translation = ["Laugh out Loud", "I don't know", "to be honest"]

#del acronym[0]
#del translation[0]
#If we were to want to delete from one list we would have to delete from both of them as they are linked


#A dictionary maps keys to values
acronyms = {"LOL" : "laugh out loud",
            "IDK" : "I don't know",
            "TBH" : "to be honest"}

#Here we have the acronyms which are assinged as keys and the translations which are assigned as the values
# The : is used as a means of saying assigned to, so LOL is assigned to laughing out loud and etc etc
#Known as key value pairs

#To find an item in a dictionary we use the key as a means of finding the value
print(acronyms["LOL"])

#Dictionaries can hold anything we want
#Dictionary of string to numbers
menu = {"Soup" : 5, "Salad" : 6}
#Dictionary of anything
my_dict = {10: "hello", 2: 6.5}



#Dictionaries are made using curly brackets.

#If you want to add something to a dictionary, you would place the name of the variable, the key in square brackets
# And then place the value after this with an equals sign,
acronyms["EMA"] = "Eat my Ass"
print(acronyms)

#We can update a value in the same way we created a new one
acronyms["EMA"] = "Eat my Apple"
print(acronyms)

#To delete a key value, we do it using del
del acronyms["EMA"]
print(acronyms)

#If you try to access a key that isnt there you will get a key error
#To avoid this we use the get method
definition = acronyms.get("BTW")
print(acronyms)
print(definition)
#By doing this we will get none instead of an error

if definition: 
    print(definition)
else: 
    print("key doesnt exist")




#So lets use this all to translate a sentance using the dictionary we have created

sentence = "IDK" + " what happened" + "TBH"
translations = acronyms.get("IDK") +" what happened "+ acronyms.get("TBH")

print("Sentence:", sentence)
print("translations:", translations)