# Issue :
# when select X or O at the start of game, game will immediately jump to player2 first
# combine get_player1_move() & get_player2_move() together
# try combine `while game_in_progress:`loop to one


# see https://inventwithpython.com/chapter10.html


def draw_board(board):
    """
    setup how does the board look like
    """
    print([board[7], board[8], board[9]])
    print([board[4], board[5], board[6]])
    print([board[1], board[2], board[3]])


def input_player_letter():
    """
    lets player 1 pick which letter to choose
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O ?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return['O', 'X']


def play_again():
    """
    this function will return True when player type y, False if type anything else
    """
    print('do you want to play again ? (y or n)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    """
    record player movement when clicked
    """
    board[move] = letter


def is_winner(brd, ltr):  # brd - board & ltr - letter
    """
    function that defines the winner
    """
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


def get_board_copy(board):
    """
    when player pick a box, duplicate board & append the changes
    """
    dupe_board = []

    for i in board:
        dupe_board.append(i)

    return dupe_board


def is_space_free(board, move):
    """
    function will return True if none of the player select this particular box
    """
    return board[move] == ''


def get_player1_move(board):
    """
    function to let player 1 type in number 1-9, on which position the user want to take
    """
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('PLAYER 1 : enter the position number 1-9 ')
        move = input()
    return int(move)


def get_player2_move(board):
    """
    function to let player 2 type in number 1-9, on which position the user want to take
    """
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('PLAYER 2 : enter the position number 1-9 ')
        move = input()
    return int(move)


def is_board_full(board):
    """
    check for board is full (Draw). return True if full, False if otherwise
    """
    for selected_move in range(1, 10):
        if is_space_free(board, selected_move):
            return False
    return True


# =========================== DONE INITIALISATION ===========================

print('Welcome to Tic Tac Toe Game!')


while True:
    the_board = [''] * 10

    player_1, player_2 = input_player_letter()

    turn = 'player 1'

    print('The ' + turn + ' will go first')
    game_in_progress = True

    while game_in_progress:
        if turn == 'player':
            draw_board(the_board)
            move = get_player1_move(the_board)
            make_move(the_board, player_1, move)

            if is_winner(the_board, player_1):
                draw_board(the_board)
                print('player 1 win')
                game_in_progress = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print("Draw, is a tie")
                    break
                else:
                    turn = 'computer'

        else:
            # player 2 move
            draw_board(the_board)
            move = get_player2_move(the_board)
            make_move(the_board, player_2, move)

            if is_winner(the_board, player_2):
                draw_board(the_board)
                print('player 2 win')
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
