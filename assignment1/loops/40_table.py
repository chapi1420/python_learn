'''40. Create a program that prompts the user for a number and
displays the table of that number using a loop.'''

#take input from the user
number = int(input('insert a number: '))

#iterate through the range of 1 to 10
for i in range(1, 11):
    #calculate the product of the number and the iterator
    product = number * i
    #display the result
    print(f'{number} x {i} = {product}')
    