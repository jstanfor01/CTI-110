# In class examples using dictionary

# Create a dictionary using key:value pairs
person1 = {"name": input("Enter name:"), "age":27, "height": 63.5}

#Get info from dictionary using the key
print(person1["height"])

#Print the entire dictionary
print(person1)
print("\n\n")

# Add key:value pair to dictionary
person1["DOB"] = "10-14-1996"
print(person1)
person1.update({'hair_color': "dark brown"})
print("\n\n")
print(person1)

# Remove a key:value pair from dictionary
del person1["height"]
print("\n\n")
print(person1)

# Create key:value pair from user input
person1["height"] = input(f"Enter height of {person1['name']}:  ")
print("\n\n")
print(person1)
print("\n\n\n")

#User picks the information to get out of dictionary
print(person1.keys(), "\n")
userChoice = input(f"What would you like to know about {person1['name']}?" )
print()
print(person1[userChoice])
