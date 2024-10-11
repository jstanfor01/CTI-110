#Joseph Stanford
#10/11/2024
#P2HW2
#Calculating lists in Grades



module1 = float(input("Enter grade for module 1: "))
module2 = float(input("Enter grade for module 2: "))
module3 = float(input("Enter grade for module 3: "))
module4 = float(input("Enter grade for module 4: "))
module5 = float(input("Enter grade for module 5: "))
module6 = float(input("Enter grade for module 6: "))

my_grades =  [module1, module2, module3, module4, module5, module6]

print(f"{'Lowest Grade':<18} {min(my_grades):<25}")
print(f"{'Highest Grade':<18} {max(my_grades):<25}")
print(f"{'Sum of Grades':<18} {sum(my_grades):<25}")

average = sum(my_grades)/len(my_grades)
print(f"{'Average':<18} {average:<25}")
