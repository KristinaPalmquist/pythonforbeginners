# find largest number in a list

# def find_max(numbers):
#     largest = 0
#     index = 0
#     for number in numbers:
#         if number > largest:
#             largest = number
#     for i in numbers:
#         index += 1
#         if i == largest:
#             print(f'Largest: {str(largest)} (index {str(index)})')


# def find_min(numbers):
#     smallest = numbers[0]
#     index = 0
#     for number in numbers:
#         if number < smallest:
#             smallest = number
#     for i in numbers:
#         index += 1
#         if i == smallest:
#             print(f'Smallest: {str(smallest)} (index {str(index)})')


def find_max(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest