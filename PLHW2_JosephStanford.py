# Joseph Stanford
# 9/24/2024
# PLHW2
# Simulating calculation of travel expenses

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

print(f"Location: {travel_destination1}")
print(f"Inital budget: {budget1}")
print(f"Fuel: {gas1}")
print(f"Accomodation: {accomodation1}")
print(f"Food: {food1}")

total = (budget1 - gas1 - accomodation1 - food1)

print(f"Remaining balance: {total}")




