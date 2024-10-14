# Joseph Stanford
# 10/14/2024
# P3HW1
# Use branching to determine letter grade
average = float(input("What is the average?"))
# Create the branching to get letter grade

if average >= 90:
    letter_grade= "A"
elif average >= 80:
    letter_grade= "B"
elif average >= 70:
    letter_grade= "C"
elif average >= 60:
    letter_grade= "D"
else:
    letter_grade = "F"

#Display the results

print(f"The average is {average:.2f}-- Letter Grade: {letter_grade}")
