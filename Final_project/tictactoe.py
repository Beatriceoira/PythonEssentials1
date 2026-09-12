from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    for row in range(3):
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(
            board[row][0], board[row][1], board[row][2]
        ))
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            
            if move < 1 or move > 9:
                print("Invalid move. Enter a number from 1 to 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] in ['X', 'O']:
                print("That square is already occupied.")
                continue

            board[row][col] = 'O'
            break

        except ValueError:
            print("Invalid move. Enter a number from 1 to 9.")


def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))

    return free


def victory_for(board, sign):
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)):
            return True

    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True

    if all(board[i][i] == sign for i in range(3)):
        return True

    if all(board[i][2 - i] == sign for i in range(3)):
        return True

    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)

    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'


board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]

display_board(board)

while True:
    enter_move(board)
    display_board(board)

    if victory_for(board, 'O'):
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    draw_move(board)
    display_board(board)

    if victory_for(board, 'X'):
        print("Computer won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
