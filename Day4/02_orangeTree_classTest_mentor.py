# Given from mentor-nicholas, NOT INSIDE STUDENT PORTAL
# Objective
# - To produce a yearly report on the tree height, how many oranges are harvested ONLY when tree is older than 5 years.
# - Stop the report when the tree dies, which is after 70 years

from random import randint


class OrangeTree():
    def __init__(self):
        self.age = 0
        self.height = 0
        self.oranges_on_tree = []

    def has_oranges(self):
        """
        function to check whether there are any oranges have grown on the tree
        """
        if len(self.oranges_on_tree) > 0:
            return True
        else:
            return False

    def grow(self):
        """
        USED RANDOM
        function to grow the tree when it run, and once the tree is older than 5 yrs, it is big enough to yield oranges.
        The tree will yield random number of oranges between 1 to 50 on every year
        """
        self.age = self.age + 1
        self.height = self.height + 4.3
        if self.age >= 5:
            for _ in range(1, randint(1, 50)):
                # if randint is 4, output is `self.oranges_on_tree.append(1)` x 4
                self.oranges_on_tree.append(1)

    def dead(self):
        """
        function when age of the tree has been more than 70 yrs, it stop the report, and print('the tree has died')
        """
        if self.age == 70:
            return True
        else:
            return False

    def pick_an_orange(self):
        """
        function when triggered (picked an orange),it will minus 1 orange from the orange tree
        """
        return self.oranges_on_tree.pop()


tree = OrangeTree()


while not tree.has_oranges():
    tree.grow()
print(f"Tree is {tree.age} years old and {tree.height} feet tall")


while not tree.dead():
    basket = []

    # It places the oranges in the basket
    while tree.has_oranges():
        basket.append(tree.pick_an_orange())

    # Assume, avg_diameter = tree height / tree age
    avg_diameter = tree.height / tree.age

    print(f"Year {tree.age} Report")
    print(f"Tree height: {int(tree.height)} feet")
    print(
        f"Harvest: {len(basket)} oranges with an average diameter of {int(avg_diameter)} inches")
    print("")
    # Age the tree another year
    tree.grow()

print("Alas, the tree, she is dead!")
