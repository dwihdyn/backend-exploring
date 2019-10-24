def binary_search(target, my_list):
    """
    Finds a target element in a sorted list using the binary search algorithm. Returns the index of the target in the list.
    """

    start = 0
    end = len(my_list) - 1

    # Find the midpoint of the list using floor division (//)
    midpoint = (start + end) // 2

    # Only end the loop when start point is larger than end point
    while not start > end:
        if target == my_list[midpoint]:
            return midpoint

        # Focus the left half of the list
        elif target < my_list[midpoint]:
            end = midpoint - 1
            midpoint = (start + end) // 2

        # Focus the right half of the list
        elif target > my_list[midpoint]:
            start = midpoint + 1
            midpoint = (start + end) // 2

    return False


print(binary_search(60, [12, 21, 33, 42, 57]))
# Round 1 - midpoint: index 2
#   60 is more than 33 (my_list[2])
#   start point is now the element after the midpoint (2 + 1)
#   Focus on index 3 onwards [42, 57]
# Round 2 - midpoint: index 3
#   60 is more than 42 (my_list)
#   start point is now index 4 (3 + 1)
#   Focus on index 4 [57]
# Round 3 - midpoint: index 4
#   60 is more than 57 (my_list[4])
#   start point is now index 5
#   HOWEVER, end point is 4
#   We can never have a situation where the start point is larger than the end point
#   Therefore, we can conclude that the target is not in the list

print(binary_search(5, [1, 2, 3, 4, 5, 6]))
