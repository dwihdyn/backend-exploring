# """
# Write a method linear_search that takes two arguments: an object and an list.

# - It should return the index of the object in the list by going through each element in sequence and returning the index of the first instance of the element.
# - If the object searched for does not exist in the list, it should return nil.
# """
# purely no function


def linear_search(target, my_list):
    pos = 0
    for i in my_list:
        if target == i:
            return print(pos)
        else:
            pos = pos + 1
    print('not found')


random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]
linear_search(18, random_numbers)  # 2 (it returns the position of the number)
linear_search(9, random_numbers)   # not found


# # # using enumerate
# # def linear_search(target, my_list):
# #     for index, val in enumerate(my_list):
# #         if target == val:
# #             print(index)  # output 18
# #             break
# #     else:
# #         print('not here')


# # random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]
# # linear_search(18, random_numbers)  # 2 (it returns the position of the number)
# # linear_search(9, random_numbers)   # not found


# # # mine with index()
# # def linear_search(target, my_list):
# #     for i in my_list:
# #         if target == i:
# #             print(my_list.index(target))  # output 18
# #             break
# #     else:
# #         print('not here')

# # random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]
# # linear_search(18, random_numbers)  # 2 (it returns the position of the number)
# # linear_search(9, random_numbers)   # not found


# # # without enumerate
# # def linear_search(target, my_list):
# #     # your code
# #     for i in range(len(my_list)):
# #         if my_list[i]== target:
# #             print(i)
# #             break
# #     else:
# #         print("nil")

# # random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]

# # linear_search(18, random_numbers)  # 2 (it returns the position of the number)
# # linear_search(9, random_numbers)   # not found
