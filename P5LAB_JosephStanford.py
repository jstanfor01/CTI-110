#Joseph Stanford
#11-19-24
#P5Lab
#Using user-defined functions

import random

def disperse_change(change):


    #Convert money to whole number
    change = round(change * 100)

    #May need to round this value
    print(change)

    #Get whole dollars from money amount
    dollars = change // 100
    print(f"Dollars: {dollars}")
    #Remove he dollar amount from money
    change = change - (dollars * 100)

    #Get quarters from money amount
    quarters = change // 25
    print(f"Quarters: {quarters}")
    #Remove he quarter amount from money
    change = change - (quarters * 25)


    #Get dimes from money amount
    dimes = change // 10
    print(f"Dimes: {dimes}")
    #Remove he quarter amount from money
    change = change - (dimes * 10)

    #Get nickels from money amount
    nickels = change // 5
    print(f"Nickels: {nickels}")
    #Remove he quarter amount from money
    change = change - (nickels * 5)

    #Get pennies from money amount
    pennies = change
    print(f"Pennies: {pennies}")



def main():
    #Logic goes here

    #Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed:.2f}")

    #Create a variable to represent money put into machine
    money_in = float(input("How much cash will you put in the self-checkout? "))

    #Calculate change owed to customer
    change = money_in - amount_owed
    print(f"Change owed: ${change: .2f}")
    disperse_change(change)
#Call the main function
main()
    
