def linear_search(target, my_list):
    """
    Finds a target element using the linear search algorithm. The index of the target is returned if it is in the list.
    """
    # Go through every single element
    for index, num in enumerate(my_list):
        # If the target is equal to the current element
        if target == num:
            # Return the index
            return index

    return False


random_numbers = [6, 29, 18, 2, 72, 19, 18, 10, 37]

# 2 (it returns the position of the number)
print(linear_search(18, random_numbers))
print(linear_search(9, random_numbers))  # not found


def global_linear_search(target, my_list):
    """
    Finds a target element in a list. Returns all the indices, if any, of the target in the list.
    """
    indices = []
    for index, letter in enumerate(my_list):
        if letter == target:
            indices.append(index)
    return indices


bananas_arr = list("bananas")  # ["b", "a", "n", "a", "n", "a", "s"]
print(global_linear_search("a", bananas_arr))  # [1, 3, 5]
