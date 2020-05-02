# Import the random module
import random


# Building and printing the board
def print_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


# Let the user pick their letter 'O' or 'X'
def the_letter():
    letter = ''
    while not (letter == 'O' or letter == 'X'):
        letter = input('Do you want to be X or O?\n').upper()
    if letter == "X":
        return ['X', 'O']
    else:
        return ['O', 'X']


# Define who will start the game
def who_starts(n):
    if random.randint(0, 1) == 0:
        return 'The computer'
    else:
        return n


# Define if the user wants to play again
def play_again():
    answer = input('Do you want to play again (Yes/No)?\n').upper()
    if answer.startswith('Y'):
        return True


# Add the correct letter to the correct spot
def make_move(board, letter, move):
    board[move] = letter


# Check if the user won the game
def is_winner(board, letter):
    return (
        (board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[7] == letter and board[8] == letter and board[9] == letter) or
        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[3] == letter and board[6] == letter and board[9] == letter) or
        (board[1] == letter and board[5] == letter and board[9] == letter) or
        (board[3] == letter and board[5] == letter and board[7] == letter)
    )


# Duplicate the board
def duplicate_board(board):
    dupl_board = []
    for n in board:
        dupl_board.append(n)
    return dupl_board


# Checks if the spot is free
def is_free(board, move):
    return board[move] == ''


# Get the user move
def get_move(board, n):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or is_free(board, int(move)):
        move = input(f'{n}, what is your next move (1-9)?\n')
        if int(move) < 1 or int(move) > 9:
            continue
        else:
            return int(move)


# Let the computer play
def get_random_move(board, moves_list):
    possible_moves = []
    for i in moves_list:
        if is_free(board, i):
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)
    else:
        return None


# Get the move from the computer
def get_computer_move(board, c_letter):
    if c_letter == 'X':
        p_letter = 'O'
    else:
        p_letter = 'X'

    # Can the computer win?
    for i in range(1, 10):
        copy = duplicate_board(board)
        if is_free(copy, i):
            make_move(copy, c_letter, i)
        if is_winner(copy, c_letter):
            return i

    # Can the user win in the next move?
    for i in range(1, 10):
        copy = duplicate_board(board)
        if is_free(copy, i):
            make_move(copy, p_letter, i)
        if is_winner(copy, p_letter):
            return i

    # Try to take one of the corners
    move = get_random_move(board, [1, 3, 7, 9])
    if move != None:
        return move

    # Try to take the center, if it is free.
    if is_free(board, 5):
        return 5

    # Move on one of the sides.
    return get_random_move(board, [2, 4, 6, 8])


def is_board_full(board):
    # Return True if every space on the board has been taken. Otherwise returns False.
    for i in range(1, 10):
        if is_free(board, i):
            return False
    return True


# Starting the game
print('Welcome to Tic Tac Toe!')
name = input('What\'s your name?\n')

while True:
    # Reset the board
    theBoard = [''] * 10
    # Assign the letter to the person and to the computer
    p_letter, c_letter = the_letter()
    turn = who_starts(name)
    print(f'{turn} starts playing!')
    game_is_playing = True

    while game_is_playing:
        if turn is not 'computer':
            # Describe player's play
            print_board(theBoard)
            move = get_move(theBoard, name)
            make_move(theBoard, p_letter, move)
            if is_winner(theBoard, p_letter):
                print_board(theBoard)
                print(f'Hooray {name}! You have won the game!')
                game_is_playing = False
            else:
                if is_board_full(theBoard):
                    print_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'computer'
        else:
            # Describe computer's play
            move = get_computer_move(theBoard, c_letter)
            print(f'Computer\'s choice: {move}')
            make_move(theBoard, c_letter, move)
            if is_winner(theBoard, c_letter):
                print_board(theBoard)
                print(f'{name}! I can\'t believe that the computer has beaten you! You lost.')
                game_is_playing = False
            else:
                if is_board_full(theBoard):
                    print(theBoard)
                    print_board(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    if not play_again():
        break
