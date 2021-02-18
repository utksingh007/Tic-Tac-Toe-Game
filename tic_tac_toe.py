# Tic-Tac-Toe Game source code

import random

# Insert X/O at position
def insert(board, ch, pos):
    board[pos] = ch

# Check if Board is full
def is_Full(board):
    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True

# Check if space is present at position
def is_Space_present(board, pos):
    if board[pos] == ' ':
        return True
    return False

# Print Board
def display_Board(board):
    print('\n\n')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('\n\n')

# Check for winner
def is_Winner(b,ch):
    if (b[1] == ch and b[2] == ch and b[3] == ch) or (b[4] == ch and b[5] == ch and b[6] == ch) or (b[7] == ch and b[8] == ch and b[9] == ch) or (b[1] == ch and b[4] == ch and b[7] == ch) or (b[2] == ch and b[5] == ch and b[8] == ch) or (b[3] == ch and b[6] == ch and b[9] == ch) or (b[1] == ch and b[5] == ch and b[9] == ch) or (b[3] == ch and b[5] == ch and b[7] == ch):
        return True
    return False

# Ask for user to make a move
def user_move(board):
    flag = 1
    while flag:
        move = str(input('Enter position:'))
        try:
            pos = int(move)
            if pos > 0 and pos < 10:
                if is_Space_present(board,pos):
                    insert(board,'X',pos)
                    flag = 0
                else:
                    print('Move already made at position.')
            else:
                print('Enter position within range! (1-9)')
        except:
            print('Not a valid number!')

# Choose a position for computer
def choose_move(moves):
    pos = random.randrange(0,len(moves))
    return moves[pos]

# Make a move for computer
def computer_move(board):
    positions_left = []
    for i in range(1,10):
        if board[i] == ' ':
            positions_left.append(i)
    move = 0
    ch = 'O'
    for i in positions_left:
        temp_Board = board[:]
        temp_Board[i] = ch
        if is_Winner(temp_Board,ch):
            move = i
            return move
    ch = 'X'
    for i in positions_left:
        temp_Board = board[:]
        temp_Board[i] = ch
        if is_Winner(temp_Board,ch):
            move = i
            return move
    corners = []
    for i in positions_left:
        if i == 1 or i == 3 or i == 7 or i == 9:
            corners.append(i)
    if corners != []:
        move = choose_move(corners)
        return move
    edges = []
    for i in positions_left:
        if i == 2 or i == 4 or i == 6 or i == 8:
            edges.append(i)
    if edges != []:
        move = choose_move(edges)
        return move
    return move

def main():
    print()
    print('Welcome to Tic-Tac-Toe Game')
    print()
    board = [' ' for i in range(10)]
    display_Board(board)
    while not(is_Full(board)):
        if not(is_Winner(board,'O')):
            user_move(board)
            display_Board(board)
        else:
            print('Computer won :(\n')
            break
        if not(is_Winner(board,'X')):
            move = computer_move(board)
            if move == 0:
                print('Tie!\n')
                break
            else:
                insert(board,'O',move)
                print('Computer made move at ',move)
                display_Board(board)
        else:
            print('You won :)\n')
            break
    if is_Full(board):
        print('Tie!\n')

while 1:
    main()
    i = int(input('Enter 1 to play agian:'))
    if i != 1:
        break