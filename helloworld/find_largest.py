# find largest number in a list

numbers = [37, 45, 1, 2, 89, 56, 3, 4, 128, 7, 5, 38, 43, 6, 7, 789, 8, 9]
smallest = numbers[0]
largest = 0
index = 0
for number in numbers:
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number
print('Largest: ' + str(largest))
print('Smallest: ' + str(smallest))
for i in numbers:
    index += 1
    if i == largest:
        print('Index of largest: ' + str(index))
    elif i == smallest:
        print('Index of smallest: ' + str(index))