# see https://inventwithpython.com/chapter10.html

import random


# prints out the board
def draw_board(board):
    # print(' | |')
    print(' ' + board[7] + '|' + board[8] + ' | ' + board[9])
    # print(' | |')
    print('----------')
    # print(' | |')
    print(' ' + board[4] + '|' + board[5] + ' | ' + board[6])
    # print(' | |')
    print('----------')
    # print(' | |')
    print(' ' + board[1] + '|' + board[2] + ' | ' + board[3])
    # print(' | |')


# lets player which letter to choose
def input_player_letter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O ?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return['O', 'X']


# randomly select which player go first, X or O | USES RANDOM
def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


# this function will return True when player type y, False if type anything else
def play_again():
    print('do you want to play again ? (y or n)')
    return input().lower().startswith('y')


# record player movement when clicked
def make_move(board, letter, move):
    board[move] = letter


# winner combinations
def is_winner(brd, ltr):  # brd - board & ltr - letter
    return(
        (brd[7] == ltr and brd[8] == ltr and brd[9] == ltr) or
        (brd[4] == ltr and brd[5] == ltr and brd[6] == ltr) or
        (brd[1] == ltr and brd[2] == ltr and brd[3] == ltr) or
        (brd[1] == ltr and brd[4] == ltr and brd[7] == ltr) or
        (brd[2] == ltr and brd[5] == ltr and brd[8] == ltr) or
        (brd[3] == ltr and brd[6] == ltr and brd[9] == ltr) or
        (brd[7] == ltr and brd[5] == ltr and brd[3] == ltr) or
        (brd[9] == ltr and brd[5] == ltr and brd[1] == ltr)
    )


# when player pick a box, duplicate board & append the changes
def get_board_copy(board):
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


# function will return True if none of the player select this particular box
def is_space_free(board, move):
    return board[move] == ''


# function to let player type in number 1-9, on which position the user want to take
def get_player_move(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('enter the position number 1-9 ')
        move = input()
    return int(move)


# for AI power-move : to enable them to move to the corner and/or center , if available | USE RANDOM
def choose_random_move_from_list(board, power_move_list):
    possible_moves = []
    for move in power_move_list:
        if is_space_free(board, move):
            possible_moves.append(move)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


# given the board & computer letter, determine where to move and return that selected move | USE RANDOM
def get_computer_move(board, comp_letter):
    if comp_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    # the AI. check if AI can win in next move
    for selected_move in range(1, 10):
        copy_board = get_board_copy(board)
        if is_space_free(copy_board, selected_move):
            make_move(copy_board, comp_letter, selected_move)
            if is_winner(copy_board, comp_letter):
                return selected_move

    # check if player can win in 1 step, block them
    for selected_move in range(1, 10):
        copy_board = get_board_copy(board)
        if is_space_free(copy_board, selected_move):
            make_move(copy_board, player_letter, selected_move)
            if is_winner(copy_board, player_letter):
                return selected_move

    # let AI to take the corner, if available
    power_move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if power_move != None:
        return power_move

    # let AI to take center, , if its available, prioritise on horizontal/vertical win combo
    if is_space_free(board, 5):
        return 5
    return choose_random_move_from_list(board, [2, 4, 6, 8])


# check for board is full (Draw). return True if full, False if otherwise
def is_board_full(board):
    for selected_move in range(1, 10):
        if is_space_free(board, selected_move):
            return False
    return True


# =========================== DONE INITIALISATION ===========================

print('Welcome to Tic Tac Toe Game!')


while True:
    the_board = [''] * 10

    # lets player which letter to choose
    player_letter, comp_letter = input_player_letter()

    # randomly select which player go first, X or O
    turn = who_goes_first()

    print('The ' + turn + 'will go first')
    game_in_progress = True

    while game_in_progress:
        if turn == 'player':
            draw_board(the_board)
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)

            if is_winner(the_board, player_letter):
                draw_board(the_board)
                print('PLAYER win')
                game_in_progress = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("Draw, is a tie")
                    break
                else:
                    turn = 'computer'

        else:
            # computer move
            move = get_computer_move(the_board, comp_letter)
            make_move(the_board, comp_letter, move)

            if is_winner(the_board, comp_letter):
                draw_board(the_board)
                print('COMPUTER win, you lose')
                game_in_progress = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("Draw, is a tie")
                    break
                else:
                    turn = 'player'

    if not play_again():
        break
