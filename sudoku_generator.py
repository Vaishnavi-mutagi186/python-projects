import random

def create_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    for i in range(9):
        numbers = list(range(1,10))
        random.shuffle(numbers)
        board[i] = numbers
    
    return board

def print_board(board):
    print("\nSudoku Board:\n")
    
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

board = create_board()
print_board(board)