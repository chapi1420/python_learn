'''Write a program that reads numbers from the user until
zero is entered, and displays the average of the numbers
entered.'''

nums = []
while True:
    num = float(input('insert a number, press 0 to stop'))
    if num==0:
        break
    nums.append(num)
sum = 0
for i in nums:
    sums += i

average = sum / len(nums)
print('average:', average)

