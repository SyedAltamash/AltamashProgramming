list = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_board(board):
    print(board[1]+ '|' +board[2]+ '|' +board[3])
    #print(         '-'           '-')
    print(board[4]+ '|' +board[5]+ '|' +board[6])
    #print(         '-'           '-')
    print(board[7]+ '|' +board[8]+ '|' +board[9])

print('Welcome to the game of Tic Tac Toe')
def player_input():
    marker = ''
    while marker!= 'X' and marker != 'O':
        marker = input('Player 1 please select your marker X or O: ')
    player1 = marker
    if player1 == 'X':
        player2 = 'O'

    else:
        player2 = 'X'

    return (player1,player2)
player1_marker,player2_marker  = player_input()


def winner(board,mark):
    if((mark ==board[1] and mark ==board[2] and mark ==board[3])or
        (mark == board[4] and mark == board[5] and mark == board[6]) or
        (mark == board[7] and mark == board[8] and mark == board[9]) or
        (mark == board[1] and mark == board[4] and mark == board[7]) or
        (mark == board[2] and mark == board[5] and mark == board[8]) or
         (mark == board[3] and mark == board[6] and mark == board[9]) or
         (mark == board[1] and mark == board[5] and mark == board[9]) or
         (mark == board[3] and mark == board[5] and mark == board[7])):
        return True
    else:
        return False

def full_board(board):
   for i in range(1,8):
       if board[i] == ' ':
        return False
   else:
       return True

while True:
        if full_board(list):
            print('Its a tie')
            break
        display_board(list)
        position = int(input('It\'s Player 1\'s turn. Enter the position of your marker (1-9): '))
        if list[position] == " ":
            list[position] = player1_marker
        elif not full_board(list):
            print("Sorry the positon is already taken.")
            continue

        if winner(list, player1_marker):
            print('Player 1 wins')
            display_board(list)
            break
        display_board(list)
        position2 = int(input('It\'s Player 2\'s turn. Enter the position of your marker (1-9): '))
        while list[position2] != " " and not full_board(list):
            print("The position is taken")
            position2 = int(input('It\'s Player 2\'s turn. Enter the position of your marker (1-9): '))
            if list[position2] == " ":
                list[position2] = player2_marker
                break
        if full_board(list):
            print('Its a tie')
            break
        else:
            list[position2] = player2_marker
        if winner(list, player2_marker):
            print('Player 2 wins')
            display_board(list)
            break



