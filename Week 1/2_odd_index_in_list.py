# Display numbers at the odd indices of a list

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("List: ", numbers_list)

print()
print("Numbers at Odd Indices of the list: ")

for i in range(len(numbers_list)):
    if i % 2 != 0:
        print(numbers_list[i])