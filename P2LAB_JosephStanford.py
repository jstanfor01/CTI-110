# Name
# 9/30/2024
# P2LAB1
# Use imported library, math, and f-string
#Import math library
import math
# Get radius from user

radius = float(input("What is the radius of the circle? "))
print()

# Calculate diameter
diameter = 2 * radius

# Display diameter with one decimal place

print(f"The diameter of the circle is {diameter:.1f}")
print()

# Calculate circumference

circum = 2 * math.pi * radius

# Display the circumference with two decimal places

print(f"The circumfercence of the circle is {circum:.2f}\n")
print()

# Calculate the area

area = math.pi * radius ** 2

print(f"The area of the circle is {area:.3f}")


