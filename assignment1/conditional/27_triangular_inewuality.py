'''Write a program that reads three numbers and tells you if they can be the
sides of a triangle (the sum of two sides must always be greater than the third
side).'''

#take the three sides of the triangle as input
sides = []
for i in range(3):
    input_side = float(input("Enter the length of side {}: ".format(i + 1)))
    sides.append(input_side)


# check if the three sides can form a triangle
if (sides[0] + sides[1] > sides[2]) and (sides[0] + sides[2] > sides[1]) and (sides[1] + sides[2] > sides[0]):
    print("The three sides can form a triangle.")
