# Joseph Stanford
# 10/2/2024
# P2LAB2
# Using dictionaries

#Create dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S": 110, "Silverado": 26}
print()

#Print all keys
print(cars.keys())
print()

#GEt a car (key) from user
userCar = input("Enter a vehicle to see its mpg: ")
print()

#Display mpg for the userCar
print(f"The {userCar} gets {cars[userCar]} mpg.")
print()

#Get miles to drive from user
miles_to_drive = int(input(f"How many miles would you like to drive the {userCar}?"))
print()

#Calculate gallons of gas needed
gallons_needed = miles_to_drive/cars[userCar]

#Display gallons of gas needed
print(f'{gallons_needed:.2f} gallon(s) of gas are needed to drive the {userCar} {miles_to_drive} miles.')

