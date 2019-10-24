"""
Task 2: Global linear search

Write a new method global_linear_search that returns a list of all the indices for the object it searches for.
In other words, if the object x is in more than one place in the list, global_linear_search will return an list containing the index of each occurrence of x.
"""

# without enumeration


def global_linear_search(target, my_list):
    pos = 0
    print(my_list)
    for i in my_list:
        if target == i:
            print(pos)
            pos = pos + 1
        else:
            pos = pos + 1


bananas_arr = list("bananas")  # ["b", "a", "n", "a", "n", "a", "s"]
global_linear_search("a", bananas_arr)   # [1, 3, 5]
