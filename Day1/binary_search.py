"""
Binary Search Task

Write a method that takes a target number and a sorted list of numbers in non-decreasing order 
and returns either the position of the number in the list, or "do not exist" to indicate the target number is not in the list.
For instance, binary_search(32, [13, 19, 24, 29, 32, 37, 43]) should return 4, since 32 is the fourth element of the list (counting from zero).
"""


def binary_search(target, my_list):

    low = 0
    high = len(my_list) - 1

    while high > low:
        if low == target:
            print(low)      # takes care when target is lowest
        elif high == target:
            print(high)     # takes care when target is highest

        # math manipulation to set guess = target |
        guess = ((target - low) / (high - low)) * (high - low)
    #   guess = (target - low)
    #   guess =  target # since low = 0 lmao

        if guess == target:
            print(guess)
            break


print(binary_search(56, list(range(1, 201))))
