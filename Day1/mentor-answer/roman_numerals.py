def roman_numerals(num):
    """
    Converts a given number to its equivalent in Roman numerals.
    """

    # Check if user input is a number
    if not num.isdigit():
        return("I asked for a positive number, not gibberish")

    # Convert input to a number
    num = int(num)

    if num > 1999:
        return('Between 1 and 1999 please!')

    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman = ["M", "CM", "D", "CD", "C", "XC",
             "L", "XL", "X", "IX", "V", "IV", "I"]

    final_answer = ""

    n = num

    # Get both the index and the value of each element in values
    for i, value in enumerate(values):
        while n >= value:
            # Append the corresponding Roman number to the final answer
            final_answer += roman[i]
            n -= value

    return(f"Your number {num} in Roman days would have been {final_answer}")


while True:
    # Get a number from the user
    num = input(
        "Type a number between 1 and 1999 to be converted to roman numeral. \nType 'exit' to exit program.\n>> ")

    # Exit the loop by breaking the loop
    if num == 'exit' or num == 'EXIT':
        break

    print(roman_numerals(num))
