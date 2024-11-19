# Python has 6 different conditional statements
# < less than
# <= less than/equal to
# == Equal to 
# >= Greater than/equal to 
# > Greater than
# != Not equal to

temp = 95 
# Assings the value of temp to 95. This is the assignment
temp == 95
# Asks the question is temp = 95. This is the comparitor

# An if statement lets us decide what to do, for example if this condition is true then do this


# Doing else, if and else if statements are much different than seen prior with JS
# Look below for how to do it as compared to JS, its way simpler

temperature = 60
if temperature > 80:
    print("It's too hot!")
    print("Stay inside!")
elif temperature < 60:
    print("It's too cold")
    print("Stay inside")
else: 
    print("Enjoy shagging your dog in platt fields park")

# what if you wanna change the programe to only say stay inside or go outside?
temperature1 = 75
if temperature1 > 80 or temperature1 < 60:
    print("Stay inside!")
else: 
    print("Enjoy bumming your kuttah")


# If you wanna add a comparison for something such as the forecast, you can
# You can use an and operator to the code to compare more than one variable case

temperature2 = 75
forecast = "sunny"

if temperature2 < 80 and forecast != "rainy":
    print("Go Outside, yours dogs ass is ripe")
else: 
    print("Stay inside!")

# Python has another logical operator called NOT, which you can use instead of !=

forecast1 = "rainy"

if not forecast1 == "rainy":
    print("Go outside")
else: 
    print("Stay inside!")

#Not is used to negate a comparison, so Not true --> False, Not false --> True



# In conclusion, python has 3 logical operators, and, or and not
# and + or are used to combine multiples comparisons
# not is used to negate a comparison


#Another data type is of course the boolean. Using the boolean will make the thing look more like english
raining6 = True

if not raining6:
    print("Go outside!")
else: 
    print("Stay inside")