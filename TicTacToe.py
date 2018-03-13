import random


def cls():
    print '\n'*50


def choose_first():
    if random.randint(0,1) == 0:
        return "Player_1"
    else:
        return "Player2"

    return "Player 1"


def space_check(board, position):
    if board[position] is None:
        return True
    else:
        return False


def full_board_check(board):
    for i in range(1,10):
        if not space_check(board, i):
            return False

    return True


def player_choice(board):

    user_position = 0

    while not (user_position in [1, 2, 3, 4, 5, 6, 7, 8, 9] or space_check(board, user_position)):
        user_position = int(raw_input('Please choose your position'))
        print "Position chosen is ", user_position
        print type(user_position)
        return user_position


def play_again():
    raw_input("Do you want to play again Y or N").upper()


# Note: Game will ignore the 0 index
def reset_board():
    global board, game_state
    # board = ['X'] * 10
    game_state = True


def display_board(board):
    # This function prints out the board so the numpad can be used as a reference
    # Clear current cell output
    # Print board
    print "  "+board[7]+" |"+board[8]+" | "+board[9]+" "
    print "------------"
    print "  "+board[4]+" |"+board[5]+" | "+board[6]+" "
    print "------------"
    print "  "+board[1]+" |"+board[2]+" | "+board[3]+" "


def player_input():

    user_input = ''

    while not (user_input == 'X' or user_input == 'O'):
        user_input = raw_input("Please enter your input").upper()
        print user_input

    if user_input == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def place_marker(board, position, marker):
    board[position] = marker


def win_check(board, player):
    # Check Horizontals,Verticals, and Diagonals for a win '''
    if (board[7] == board[8] == board[9] == player) or \
        (board[4] == board[5] == board[6] == player) or \
        (board[1] == board[2] == board[3] == player) or \
        (board[7] == board[4] == board[1] == player) or \
        (board[8] == board[5] == board[2] == player) or \
        (board[9] == board[6] == board[3] == player) or \
        (board[1] == board[5] == board[9] == player) or \
            (board[3] == board[5] == board[7] == player):
        return True
    else:
        return False


''' reset_board()

val = player_input()

print "the value is ", val

display_board()


final_result = win_check(board, 'X')

print final_result '''


print "Welcome to Tic Tac Toe"

while True:

    board = [' ']*10
    player_1_marker, player_2_marker = player_input()

    turn = choose_first()
    print turn + ' will go first'

    play_game = ''

    while not (play_game == 'Y' or play_game == 'N'):
        play_game = raw_input('Ready to play ? Y or N').upper()
        print play_game

    if play_game == 'Y':
        game_on = True

    else:
        game_on = False

    while game_on:

        if turn == 'Player 1':

            position = player_choice(board)

            print "player 1 input is  ", player_1_marker
            print "player 2 input is  ", player_2_marker

            place_marker(board, position, player_1_marker)

            if win_check(board, player_1_marker):
                display_board(board)
                print "Player 1 has Won"
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print "It's a Tie"
                    game_on = False
                else:
                    cls()
                    display_board(board)
                    turn = 'Player 2'

        else:

            position = player_choice(board)

            place_marker(board, position, player_2_marker)

            if win_check(board, player_2_marker):
                display_board(board)
                print "Player 2 has Won"
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print "It's a Tie"
                    game_on = False
                else:
                    cls()
                    display_board(board)
                    turn = 'Player 1'

















