# #remove duplicates in list
# numbers = [1, 3, 1, 5, 3, 7, 5, 5, 5, 5, 7, 3]
# index_number = -1
# for number in numbers:
#     index_number += 1
#     index_compare = -1
#     print('i: ' + str(index_number))
#     for compare in numbers:
#         index_compare += 1
#         print('j: ' + str(index_compare))
#         if number == compare and index_number != index_compare:
#             numbers.pop(index_compare)
   
# print(numbers)


numbers = [1, 21,  3, 1, 5, 3, 7, 5, 5, 5, 5, 7, 3]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
numbers = uniques.copy()
print(numbers)
