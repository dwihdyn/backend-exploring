"""
This program can take in a number and will print the following as your result:

The program will ask you for a number
Fizz: if the number you pass in is a multiple of 3 eg. 3,6,9,12....
Buzz: if it is a multiple of 5 eg. 5,10,20....
FizzBuzz: if it is a multiple of 5 and 3 eg. 15, 30....
Print the number from the user if the number passed in is neither a multiple of 3 nor 5


Expected Behavior...
If I input 6 ➡ Fizz
If I input 10 ➡ Buzz
If I input 15 ➡ FizzBuzz
If I input 8 ➡ 8
Don't hardcode the logic, use the modulo operator!
"""
selected_number = 6

if (selected_number % 3 == 0 and selected_number % 5 == 0):
    print("Fizz Buzz")
elif selected_number % 5 == 0:
    print("Buzz")
elif selected_number % 3 == 0:
    print("Fizz")
else:
    print(selected_number)
