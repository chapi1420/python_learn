'''Create a program that prompts the user for a number and
displays the table of that number using a loop.'''

number = int(input('Enter a number: '))
print('---------------------')
for i in range(1, number + 1):
    for j in range(1, number + 1):
        print(f'{i} * {j} = {i * j}')
    
    print('-'*20)