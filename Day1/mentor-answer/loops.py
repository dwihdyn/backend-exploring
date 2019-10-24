# Longest name
names = ['Sheng', 'Kevin', 'Audrey', 'KJ', 'Delilah', 'Josh', 'Mack', 'Rey']
# keep track the name that is currently the longest
longest_name = ''

# go through each of the name in the names list
for name in names:
    # if the current element is longer than the longest name
    if len(name) > len(longest_name):
        # replace longest name with the current element
        longest_name = name

print(longest_name)


# ---------------------------------

# List comprehensions
# The long way
# def long_words(lst):
#     words = []
#     for word in lst:
#         if len(word) > 5:
#            words.append(word)
#     return words


def longer_than_five(lst):
    """
    Finds and returns a list of words that are longer than 5 characters long.
    """
    # Syntax: [<expression> <loop> <conditional>]
    # expression: word (because we want word)
    # loop: for word in lst (we are looping through lst)
    # conditional: if len(word) > 5
    return [word for word in lst if len(word) > 5]


print(longer_than_five(names))

# ---------------------------------

# Loop challenge
info = [
    ["name", "age", "pet"],
    ["Amy", "20", "bird"],
    ["John", "21", "cat"],
    ["Ash", "24", "dog"],
]

# What the final answer should look like
# class_info = {
#   "0": {"name": "Amy", "age": 20, "pet": "bird"},
#   "1": {"name": "John", "age": 21, "pet": "cat"},
#   "2": {"name": "Ash", "age": 24, "pet": "dog"},
# }

# Obtain the keys to construct the dictionary with
keys = info[0]

students = info[1:]

class_info = {}

for id, student in enumerate(students):
    # Keep track of each student's info in a dictionary
    student_info = {}

    for index, key in enumerate(keys):
        student_info[key] = student[index]
    class_info[str(id)] = student_info

print(class_info)
