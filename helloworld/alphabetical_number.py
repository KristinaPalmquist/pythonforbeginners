# phone = input('What is your phone number? ')
# new = phone.replace('0', 'Zero ').replace('1', 'One ').replace('2', 'Two ').replace('3', 'Three ').replace('4', 'Four ').replace('5', 'Five ').replace('6', 'Six ').replace('7', 'Seven ').replace('8', 'Eight ').replace('9', 'Nine ')
# print(new)

phone = input('Phone: ')
digits_mapping = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}
output = ''
for char in phone:
    output += digits_mapping.get(char, '!') + ' '
print(output)