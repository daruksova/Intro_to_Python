# Задача 4*. (Необязательная). Создайте игру в крестики-нолики.

def draw_board(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-+-+-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-+-+-')
    print(board[6] + '|' + board[7] + '|' + board[8])

def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
       (board[3] == player and board[4] == player and board[5] == player) or \
       (board[6] == player and board[7] == player and board[8] == player) or \
       (board[0] == player and board[3] == player and board[6] == player) or \
       (board[1] == player and board[4] == player and board[7] == player) or \
       (board[2] == player and board[5] == player and board[8] == player) or \
       (board[0] == player and board[4] == player and board[8] == player) or \
       (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False

def play_game():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    players = ['X', 'O']
    current_player = 0
    winner = False

    while not winner and ' ' in board:
        draw_board(board)
        print('Player ' + players[current_player] + ' turn')
        position = int(input('Choose a position (1-9): ')) - 1
        if board[position] == ' ':
            board[position] = players[current_player]
            winner = check_win(board, players[current_player])
            current_player = (current_player + 1) % 2
        else:
            print('Position already taken, try again')

    draw_board(board)
    if winner:
        print('Player ' + players[current_player] + ' wins!')
    else:
        print('Game ended in a draw')

play_game()