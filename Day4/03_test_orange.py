# Given from mentor-nicholas, NOT INSIDE STUDENT PORTAL


class OrangeTree():
    def __init__(self):
        self.oranges = []
        self.age = 0    # zero starting age
        self.height = 0  # zero starting height

    def has_oranges(self):
        if len(self.oranges) > 0:
            return True
        else:
            return False

    def grow(self):
        self.age = self.age + 1
        if self.age >= 5:
            self.oranges.append(1)

    def dead(self):
        if self.age == 8:
            return True

    def pick_an_orange(self):
        return self.oranges.pop()


tree = OrangeTree()


# baby tree
while not tree.has_oranges():
    tree.grow()
print(f"Tree is {tree.age} years old and {tree.height} feet tall")


# adult tree
while not tree.dead():
    basket = []

    # It places the oranges in the basket
    while tree.has_oranges():  # false if self.oranges = []
        basket.append(tree.pick_an_orange())

    # It's up to you to calculate the average diameter for the new oranges
    avg_diameter = 2

    print(f"Year {tree.age} Report")
    print(f"Tree height: {tree.height} feet")
    print(
        f"Harvest: {len(basket)} oranges with an average diameter of {avg_diameter} inches")
    print("")

    # Age the tree another year
    tree.grow()

print("Alas, the tree, she is dead!")
