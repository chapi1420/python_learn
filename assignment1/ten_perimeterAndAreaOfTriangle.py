'''
Write a program that calculates the perimeter and area of a
triangle, using the formulas P = a + b + c and A = (b * h) / 2,
where a, b and c are the sides of the triangle and h is the height
relative to the side B.'''
# Prompt the user for the lengths of the sides of the triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
# Prompt the user for the height of the triangle relative to side b
h = float(input("Enter the height of the triangle relative to side b: "))
# Calculate the perimeter of the triangle using the formula P = a + b + c
perimeter = a + b + c
#calculate the area of the triangle using the formula A = (b * h) / 2
area = (b * h) / 2
# Display the results
print("The perimeter of the triangle is: ", perimeter)
print("The area of the triangle is: ", area)
