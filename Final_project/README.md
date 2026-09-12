# Instruction

## Scenario

Your task is to write a simple program which pretends to play tic-tac-toe with the user. To make it all easier for you, we've decided to simplify the game. Here are our assumptions:

    the computer (i.e., your program) should play the game using 'X's;
    the user (e.g., you) should play the game using 'O's;
    the first move belongs to the computer − it always puts its first 'X' in the middle of the board;
    all the squares are numbered row by row starting with 1 (see the example session below for reference)
    the user inputs their move by entering the number of the square they choose − the number must be valid, i.e., it must be an integer, it must be greater than 0 and less than 10, and it cannot point to a field which is already occupied;
    the program checks if the game is over − there are four possible verdicts: the game should continue, the game ends with a tie, you win, or the computer wins;
    the computer responds with its move and the check is repeated;
    don't implement any form of artificial intelligence − a random field choice made by the computer is good enough for the game.

The example session with the program may look as follows:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 1
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 8
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 4
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move: 7
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   X   |   X   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   O   |   O   |   9   |
|       |       |       |
+-------+-------+-------+
You won!


## Requirements

Implement the following features:

    the board should be stored as a three-element list, while each element is another three-element list (the inner lists represent rows) so that all of the squares may be accessed using the following syntax:


board[row][column]
 


    each of the inner list's elements can contain 'O', 'X', or a digit representing the square's number (such a square is considered free)
    the board's appearance should be exactly the same as the one presented in the example.
    implement the functions defined for you in the editor.


Drawing a random integer number can be done by utilizing a Python function called randrange(). The example program below shows how to use it (the program prints ten random numbers from 0 to 8).

Note: the from-import instruction provides access to the randrange function defined within an external Python module callled random.

from random import randrange
 
for i in range(10):
    print(randrange(8))


# Description

A simple command-line Tic-Tac-Toe game written in Python. You play against the computer, with the player using O and the computer using X.

## Features
- Play Tic-Tac-Toe directly in the terminal.
- Player moves are entered using numbers 1–9.
- The computer chooses its moves randomly.
- Detects wins for both the player and computer.
- Detects tied games.
- Prevents invalid or occupied moves.

## System Requirements
Python 3.x
No external libraries are required.
The project uses Python's built-in random module.

## How to Play

Run the Python file from your terminal:

python tic_tac_toe.py


The board is displayed using numbers to identify each square:

+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+


Enter the number corresponding to the square where you want to place your O.

For example:

Enter your move: 1


The computer will then automatically make its move using X.


## Board Positions

The positions are numbered as follows:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

## Game Rules
- The player is O.
- The computer is X.
- Players take turns placing their symbol on an empty square.
- The first player to get three symbols in a row wins.
- A winning row can be:
Horizontal
Vertical
Diagonal
- If all squares are filled without a winner, the game ends in a tie.

## Code Overview
display_board(board)

Displays the current game board in a formatted grid.

enter_move(board)

Handles the player's input and validates the selected move.

It checks that:

- The input is a number.
- The number is between 1 and 9.
- The selected square is not already occupied.

The player's symbol O is then placed on the board.

make_list_of_free_fields(board)

Finds all empty squares on the board and returns their row and column positions.

Example:

[(0, 0), (0, 1), (0, 2)]

victory_for(board, sign)

Checks whether the specified player has won.

It checks all:

- Rows
- Columns
- Main diagonal
- Opposite diagonal
- draw_move(board)

Makes the computer's move.

The computer:

- Finds all available squares.
- Randomly selects one.
- Places X in that square.
- Starting Board

The game starts with the center square occupied by the computer:

board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
]


This means the computer has already placed X in position 5 before the first player move.

Example Game
Enter your move: 1

+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+


The computer then selects an available square at random.

## License

This project is intended for educational and personal use.
