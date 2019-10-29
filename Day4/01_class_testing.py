# class BankAccount():
#     def __init__(self, bal, cli_name):
#         self.client_name = cli_name
#         self.balance = bal

#     def deposit(self, amt):
#         self.balance = self.balance + amt

#     def activate_account(self):
#         self.status = 'yes'

# # ========================================================================================================


# john_bank_acc = BankAccount(cli_name="John Park", bal=10)
# print(john_bank_acc)
# print(john_bank_acc.client_name)
# print(f"initial balance {john_bank_acc.balance}")

# john_bank_acc.activate_account()

# john_bank_acc.deposit(100)
# print(f"account activated ? {john_bank_acc.status} ")
# print(f"first deposit {john_bank_acc.balance}")

# john_bank_acc.deposit(300)
# print(f"second deposit {john_bank_acc.balance}")


# # ========================================================================================================
# print("=====USING CLASS ATTRIBUTE=====")
# # ========================================================================================================


# class Dog():
#     species = 'mammals'  # all types of dogs are mamals

#     def __init__(self, breed, name):
#         self.dog_breed = breed
#         self.dog_name = name


# my_dog = Dog('shibe', 'doggo')
# neighbour_dog = Dog('lamer than mine', 'many wow')

# print(my_dog.dog_breed)
# print(my_dog.dog_name)
# # notice the species always the same, since we let species as class attr, not instance attr
# print(my_dog.species)

# print(neighbour_dog.dog_breed)
# print(neighbour_dog.dog_name)
# # notice the species always the same, since we let species as class attr, not instance attr
# print(neighbour_dog.species)


# ========================================================================================================
print("=====INHERITANCE METHOD=====")
# ========================================================================================================


class Animal():
    def __init__(self, food):
        self.food = food
        print('new animal created!')

    # all animals must eat, hence we create this inside parents class Animal()
    def feed(self):
        print(f"Feeding {self.food}")


# since dog is part of animal, we can inherit what animal(parent) have to dog(child) class
class DogFamily(Animal):
    def __init__(self, breed, name, food):
        Animal.__init__(self, food)  # method to override Animal(parent) class
        self.dog_breed = breed
        self.dog_name = name

    def walk(self):
        print(f"{self.dog_name} wants to have a walk")


# since cat is also part of animal, cat (child) class can inherit from animal (parent) class
class CatFamily(Animal):
    def __init__(self, color, name, food):
        Animal.__init__(self, food)
        self.cat_color = color
        self.cat_name = name

    def scratch(self):
        print(f"{self.cat_name} scratch you!")


# will print out 'new animal created' thanks to Animal.__init__
my_dog1 = DogFamily('golden retriever', 'smart_doggo', 'bone')
my_dog1.walk()
my_dog1.feed()  # empty bc we have define the food inside the DogFamily() __init__, we just need to CALL it


my_cat = CatFamily('orange', 'bitch', 'salmon')
my_cat.scratch()
my_cat.feed()
# my_cat.walk()  # expect undefined, since walk is defined in DogFamily only, not in CatFamily or Animal() class_attribute


# # ========================================================================================================
# print("=====OVERRIDE BUILD-IN FUNCTIONS TOWARDS CLASS=====")
# # ========================================================================================================

# print("=== OVERRIDE len() __len__ & print() __str__ to class ===")


# class Book():
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __len__(self):  # override len() function with our new function
#         return self.pages

#     def __str__(self):  # override print() function . can use __repr__ instead of __str__ in flask
#         return f"{self.title} that has {self.pages} pages, is written by {self.author}"


# my_book = Book('Billion Dollar Whale', 'Some guy', 400)

# print(len(my_book))
# print(my_book)
