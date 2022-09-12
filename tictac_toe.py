# This is the Tic Tac Toe game
# Coded by Charles Nguyen
# Date: 08/16/2022
import random


def display_board(board):

    # To clear the old table ( If we have table) by jumping 100 blank spaces
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# Take the input to decide will be which marker
def player_input():

    # Assign marker as empty space
    marker = ''

    # Check that marker that input is X or O, if not, continue doing the loop
    while not (marker == 'X' or marker == 'O'):

        # Upper function will turn every character input into upper case
        marker = input('Player 1: Choose X or O: ').upper()

    # Return as a tuple
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Place the marker on the board
def place_marker(board, marker, position):

    # Assign marker to position on board
    board[position] = marker


# Check who win
def win_check(board, mark):

    # Track list to store all the index of the mark in the board
    track = [x for x in range(len(board)) if board[x] == mark]

    # Win_base list contains all the index possible that
    # could lead to the winning condition
    win_base = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9],
                [1, 5, 9], [3, 5, 7]]

    # Check all the condition by taking list element group of 3
    # and compare that if track contains all elements of win_list elements
    for win_list in win_base:
        if all(x in track for x in win_list):
            return True
    return False


# Choose who will go first base on randomly
def choose_first():

    # Random the number to choose randomly
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# Condition function to check that there is space in that position
def space_check(board, position):

    return board[position] == ' '


# Check if the board is full or not
def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    # Board is full so we return True
    return True


# Take the input of position on the board for each player
def player_choice(board, name):

    # Assign the position is 0 at beginning to proc the while loop
    run = True

    # Loop condition in which not in the position have already had or the board is not full
    # Then we can take the input
    while True:
        position = input('Please choose a position, ' + name + ' : (1-9) ')
        try:
            position = int(position)
            if position in range (1,10):
                if space_check(board, position):
                    run = False
                else:
                    print('This place is occupied')
            else:
                print( name + ', please choose a number between (1-9)')
        except:
            print('Please choose a number')
    return position


# Check if they want to replay or not
def replay():

    choice = input('Play again? Enter Yes or No? : ').upper()

    return choice == 'YES'


# MAIN PROGRAM IS HERE!!

# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to TIC TAC TOE')

while True:

    # PLAY THE GAME

    # SET EVERYTHING UP (BOARD, WHO'S FIRST, CHOSE MARKERS)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? : ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # GAME PLAY
    while game_on:

        # Player ONE turn
        if turn == 'Player 1':

            # Show the board
            display_board(the_board)

            # Choose the position
            position = player_choice(the_board, 'Player 1')

            # Place the marker on the position

            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON !!')
                game_on = False

            # Check if there are still space on the board
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    break
                else:
                    turn = 'Player 2'

        # Player TWO turn
        else:

            # Show the board
            display_board(the_board)

            # Choose the position
            position = player_choice(the_board, 'Player 2')

            # Place the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON !!')
                game_on = False
            else:

                # Check if there are still space on the board
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!!')
                    break
                else:
                    turn = 'Player 2'
    if not replay():
        break
