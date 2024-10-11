# Joseph Stanford
# 10/11/2024
# P2HW2
# Formatting travel expenses

print(" This program calculates and displays travel expenses")
print()

#Get info for travel destination

budget1 = int(input("Enter budget: "))
travel_destination1 = input("Enter your travel destination: ")
gas1 = int(input("How much do you think you will spend on gas? "))
accomodation1 = int(input("Aproximately, how much will you need for accomadation/hotel? "))
food1= int(input("Last, how much do you need for food: "))
print()




print("-------Travel Expenses------")
print()
print()

print(f"{'Location': <18}{travel_destination1: <25}")
print(f"{'Inital budget':<18}{budget1:<25}")
print(f"{'Fuel':<18} {gas1:<25}")
print(f"{'Accomodation':<18}{accomodation1:<25}")
print(f"{'Food':<18}{food1:<25}")

print("-" * 25)
total = (budget1 - gas1 - accomodation1 - food1)
print()
print()
print(f"Remaining balance: {total}")




