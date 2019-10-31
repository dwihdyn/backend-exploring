# https://github.com/yi-mei-wang/boggle : find the code parts on each level, and build level by level

# Boggle rule :
# shakes the whole board, that will shake the dice inside it -> find the words in it, horizontally, vertically, diagonally

# Level 1:
# Print a 4 x 4 board
# - Shuffle dice
# - Choose a random side of each die
# - Print it out
# - Get user input


# Level 2:
# Find a word horizontally : using for i in horizontal_coordinate, for j in vertical_coordinate


# Level 3:
# Find a word vertically


# Level 4:
# Find a word in all directions

# ===================================================================================================================
import random

DICE = ["AJSIE", "ISNEW", "PWOUA", "HSIEN"]


def empty_board(board_size):
    """
    Return an empty board_size * board_size board
    """
    board = []
    for _ in range(board_size):
        board.append([''] * board_size)
    return board


def shake(dice, board):
    row = 0

    for index in enumerate(dice):
        col = index % 4

        board[row][col]


print(empty_board(4))
print(DICE)
