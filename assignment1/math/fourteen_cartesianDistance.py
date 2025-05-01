'''14. Write a program that reads the x and y position of two
points in the Cartesian plane, and calculates the distance
between them.'''

#take input of the two points
x1 = float(input("Enter the x coordinate of the first point: "))
y1 = float(input("Enter the y coordinate of the first point: "))
x2 = float(input("Enter the x coordinate of the second point: "))
y2 = float(input("Enter the y coordinate of the second point: "))
#calculate the distance between the two points
X_distance = x2 - x1
Y_distance = y2 - y1
distance = (X_distance ** 2 + Y_distance ** 2) ** 0.5
#display the result
print("The distance between the two points is: ", distance)