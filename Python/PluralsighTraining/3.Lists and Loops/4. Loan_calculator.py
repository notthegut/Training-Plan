#Get details of loan from user

money_owed = float(input("How much money do you owe, in pounds?\n")) #50,000
apr = float(input("What is the annual percentage rate of the loan?\n")) #3%
payment = float(input("How much will you pay off each month?\n")) #1,000
months = int(input("How many months do you want to see the results for?\n"))#24

monthly_rate = apr/100/12

#loop range done to find the amount owed after 24 months for the same monthly payments and interest rate
for i in range(months):

    #Calculate interest to pay
    interest_paid = money_owed*monthly_rate
    #Add in the interest
    money_owed = money_owed + interest_paid

    if(money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, "months")
        break
    #This is put in to have it so that when the loan is paid off, the line of code stops and doesnt repeatedly run, to avoid giving a negative number
    #Make payment
    money_owed = money_owed - payment

    print("Paid", payment, "of which", interest_paid, "was interest", end ="")
    #end done as a space so that they are on the same line
    print("Now I Owe", money_owed)