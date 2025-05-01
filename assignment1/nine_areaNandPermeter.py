'''Write a program that calculates the perimeter and area of a
rectangle, using the formulas P = 2(w + l) and A = wl, where w
is the width and l is the length'''
# take input of the length and width of the rectange
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# calculate the area of the rectangle
area = length * width
# calculate the perimeter of the rectangle
perimeter = 2 * (length + width)
# display the results
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)