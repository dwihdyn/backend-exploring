# https://code.nextacademy.com/lessons/roman-numerals/399

roman_numerals = {
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}

normal_no = int(input('enter number between 1 to 3999 : '))
roman_no = ''
prog = normal_no


for val in roman_numerals:
    while prog >= roman_numerals.get(val):
        prog = prog - roman_numerals.get(val)
        roman_no = roman_no + val

print(f"{roman_no} is the roman number of {normal_no}")


# without for loop
# while progress != 0:
#     if progress >= 10:
#         progress = progress - 10
#         roman_no = roman_no + 'X'
#     elif progress >= 9:
#         progress = progress - 9
#         roman_no = roman_no + 'IX'
#     elif progress >= 5:
#         progress = progress - 5
#         roman_no = roman_no + 'V'
#     elif progress >= 4:
#         progress = progress - 4
#         roman_no = roman_no + 'IV'
#     elif progress >= 1:
#         progress = progress - 1
#         roman_no = roman_no + 'I'
# print(f"{roman_no} is the roman number of {normal_no}")
