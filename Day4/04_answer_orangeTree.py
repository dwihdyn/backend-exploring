from random import randint


class Orange():
    def __init__(self):
        self.diameter = randint(1, 5)


class OrangeTree():
    def __init__(self):
        self.age = 0
        self.height = 0
        self.oranges = []

    def has_oranges(self):
        if len(self.oranges) > 0:
            return True
        else:
            return False

    def grow(self):
        self.age += 1
        self.height += 2
        if self.age >= 5:
            for _ in range(0, randint(0, 100)):
                self.oranges.append(Orange())

    def dead(self):
        if self.age > 50:
            return True
        else:
            return False

    def pick_an_orange(self):
        return self.oranges.pop()


tree = OrangeTree()

while not tree.has_oranges():
    tree.grow()

print(f"Tree is {tree.age} years old and {tree.height} feet tall")

while not tree.dead():
    basket = []

   # It places the oranges in the basket
    while tree.has_oranges():
        basket.append(tree.pick_an_orange())

    # It's up to you to calculate the average diameter for this harvest.
    avg_diameter = 1

    print(f"Year {tree.age} Report")
    print(f"Tree height: {tree.height} feet")
    print(
        f"Harvest: {len(basket)} oranges with an average diameter of {avg_diameter} inches")
    print("")

    # Age the tree another year
    tree.grow()

print("Alas, the tree, she is dead!")
