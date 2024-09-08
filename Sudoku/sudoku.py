# Sudoku
import random
import copy
import os
os.system("clear")
print("Sudoku Solver\n")

CLEAR = "\033[2K"

# 6x6 Easy
board_6_easy = [
[0, 3, 0, 4, 0, 0],
[0, 0, 5, 6, 0, 3],
[0, 0, 0, 1, 0, 0],
[0, 1, 0, 3, 0, 5],
[0, 6, 4, 0, 3, 1],
[0, 0, 1, 0, 4, 6]
]

# 6x6 Medium
board_6_medium = [
[6, 2, 0, 5, 0, 3],
[0, 0, 0, 0, 0, 0],
[5, 0, 0, 0, 3, 0],
[0, 6, 0, 0, 2, 0],
[0, 0, 0, 3, 4, 6],
[3, 0, 6, 0, 0, 0]
]

# 6x6 Hard
board_6_hard = [
[0, 0, 5, 0, 0, 2],
[6, 0, 0, 0, 0, 0],
[4, 0, 0, 0, 0, 5],
[5, 0, 0, 0, 4, 0],
[0, 0, 1, 2, 0, 0],
[0, 0, 0, 0, 0, 1]
]

# 9x9 Easy
board_9_easy = [
[0, 7, 0, 5, 8, 3, 0, 2, 0],
[0, 5, 9, 2, 0, 0, 3, 0, 0],
[3, 4, 0, 0, 0, 6, 5, 0, 7],
[7, 9, 5, 0, 0, 0, 6, 3, 2],
[0, 0, 3, 6, 9, 7, 1, 0, 0],
[6, 8, 0, 0, 0, 2, 7, 0, 0],
[9, 1, 4, 8, 3, 5, 0, 7, 6],
[0, 3, 0, 7, 0, 1, 4, 9, 5],
[5, 6, 7, 4, 2, 9, 0, 1, 3]
]

# 9x9 Medium
board_9_medium = [
[0, 4, 0, 0, 8, 0, 6, 5, 9],
[0, 2, 0, 4, 1, 0, 0, 8, 0],
[0, 0, 8, 6, 0, 0, 4, 1, 2],
[0, 6, 0, 3, 4, 0, 0, 0, 5],
[0, 9, 0, 0, 6, 8, 0, 3, 0],
[0, 8, 0, 0, 0, 9, 1, 6, 7],
[9, 7, 6, 0, 0, 2, 0, 4, 1],
[0, 0, 4, 0, 0, 0, 5, 0, 0],
[0, 0, 5, 0, 0, 4, 0, 0, 0]
]

# 9x9 Hard
board_9_hard = [
[0, 5, 0, 0, 1, 0, 0, 0, 7],
[0, 0, 7, 0, 3, 6, 9, 0, 5],
[0, 3, 0, 0, 0, 0, 0, 0, 0],
[4, 0, 0, 0, 0, 3, 0, 5, 2],
[0, 0, 0, 0, 4, 0, 0, 0, 9],
[0, 7, 9, 0, 0, 2, 1, 0, 0],
[0, 0, 0, 2, 0, 0, 0, 9, 1],
[0, 6, 0, 7, 0, 0, 0, 2, 0],
[5, 0, 0, 0, 0, 0, 0, 4, 0]
]

# Choose which board you want to solve
# board_6_easy
# board_6_medium
# board_6_ hard
# board_9_easy
# board_9_medium
# board_9_hard

board = board_6_easy

# Returns the column as a list
def get_column(board, c):
    column = []
    for r in range(len(board)):
        column.append(board[r][c])
    return column

# Returns the possible options for each cell
def get_options(board, r, c):
    # Check if the cell already has a number
    if board[r][c] != 0:
        return []
    
    # Start with full list of options (Ex 1-6)
    options = [i for i in range(1, len(board) + 1)]
    
    # Get the current row
    row = board[r]
    
    # Get the current column
    col = get_column(board, c)
    
    # For each number in the row, remove it from the possible options
    for num in row:
        if num in options:
            options.remove(num)
    
    # For each number in the column, remove it from the possible options
    for num in col:
        if num in options:
            options.remove(num)
    
    # Return the remaining options
    return options

# Checks 6x6 and 9x9 boards to see if they is solved correctly
# Returns True or False
def check_board(board):
    # Check rows
    for r in range(len(board)):
        options = [i for i in range(1, len(board) + 1)]
        row = board[r]
        for c in range(len(row)):
            val = board[r][c]
            if val == 0:
                return False
            if val in options:
                options.remove(val)
        if len(options) != 0:
            return False
        
    # Check cols
    for c in range(len(board[0])):
        options = [i for i in range(1, len(board) + 1)]
        col = get_column(board, c)
        for r in range(len(col)):
            val = board[r][c]
            if val == 0:
                return False
                
            if val in options:
                options.remove(val)
                
        if len(options) != 0:
            return False   
    
    # Check regions
    # 6x6
    if len(board) == 6:
        regions = ((0, 0), (0, 3), (2, 0), (2, 3), (4, 0), (4, 3))
        width = 2
        height = 3
    
    # 9x9
    if len(board) == 9:
        regions = ((0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6))
        width = 3
        height = 3
        
    for region in regions:
        options = [i for i in range(1, len(board) + 1)]
        for r in range(0, width):
            for c in range(0, height):
                # Calculate offset
                rr = r + region[0]
                rc = c + region[1]
                
                val = board[rr][rc]
                if val == 0:
                    return False
                if val in options:
                    options.remove(val)
                    
        if len(options) != 0:
            return False   
                
    return True

# Print the board
def print_board(board):
    for r in range(0, len(board)):
        for c in range(0, len(board[0])):
            print(f"{board[r][c]} ", end='')
        print()
    print()

print_board(board)

# Use available options only

count = 0

while True:
    # Count how many iterations
    # Print every 10,000
    count = count + 1
    if count % 1000 == 0:
        print(f"{CLEAR}\rOngoing Attempts: {count:,}", end='', flush=True)
    
    # Create a deep copy of the board
    temp = copy.deepcopy(board)
    
    # For each cell
    can_be_solved = True
    for r in range(0, len(temp)):
        if not can_be_solved:
            break
        for c in range(0, len(temp[0])):
            if not can_be_solved:
                break
                
            # Check if the cell is empty
            # If so, check for options
            if temp[r][c] == 0:
                # Get the available options for that cell
                options = get_options(temp, r, c)
                
                # If there are no options, it cannot be solved
                if len(options) == 0:
                    can_be_solved = False
                else:
                    option = random.choice(options)
                    temp[r][c] = option
                    options.remove(option)

    if can_be_solved:
        solved = check_board(temp)
        if(solved):
            print("\nSOLVED!\n")
            break
        
print_board(temp)
print(f"Total Attempts: {count:,}")

