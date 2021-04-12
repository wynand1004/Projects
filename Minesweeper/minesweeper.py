# Minesweeper Part 1 Basic Game Functions
# Simple Minesweeper Game
# Python 3.x Compatible
# Windows, MacOSX, and Linux Compatible
# by @TokyoEdtech

# Declare constants
EMPTY = 0
MINE = 1
UNKNOWN = -1
FLAG = -2

grid = [
    [0,0,0,0,0,0,0,0,0],
    [0,1,0,0,0,0,0,1,0],
    [1,0,1,0,0,0,1,0,0],
    [1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0],
    [0,1,0,1,1,0,0,0,0],
    [0,0,1,0,0,0,1,1,1],
    [1,0,0,0,0,1,0,0,0],
    [0,0,1,0,1,0,0,0,0]
]

player_grid = [
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1]
]

def count(row, col):
    offsets = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
    count = 0
    for offset in offsets:
        offset_row = row + offset[0]
        offset_col = col + offset[1]
        
        # Check for boundaries
        if((offset_row>=0 and offset_row<=8) and (offset_col>=0 and offset_col<=8)):
            if grid[offset_row][offset_col] == MINE:
                count += 1
    return count
        

def click(row, col):
    # Check if it is a bomb
    if grid[row][col] == MINE:
        print("BOOM!")
    elif player_grid[row][col] == UNKNOWN:
        player_grid[row][col] = count(row, col) 
        
        # Find all connected cells and their values
        cells = [(row, col)]
        offsets = ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1))
        
        while len(cells) > 0:
            cell = cells.pop()
            for offset in offsets:
                row = offset[0] + cell[0]
                col = offset[1] + cell[1]
                if((row>=0 and row<=8) and (col>=0 and col<=8)):
                    if((player_grid[row][col]==UNKNOWN) and (grid[row][col]==EMPTY)):
                        player_grid[row][col] = count(row,col)

                        if count(row,col) == EMPTY and (row,col) not in cells:
                            cells.append((row,col))
                        else:
                            player_grid[row][col] = count(row,col)
    
def set_flag(row, col):
    if player_grid[row][col] == UNKNOWN:
        player_grid[row][col] = FLAG
    elif player_grid[row][col] == FLAG:
        player_grid[row][col] = UNKNOWN

def show_grid():
    symbols = {-2:"F", -1:"."}
    for row in range(len(player_grid)):
        for col in range(len(player_grid[row])):
            value = player_grid[row][col]
            if value in symbols:
                symbol = symbols[value]
            else:
                symbol = str(value)
            print(f"{symbol} ", end='')
        print("")
    


# TESTING CODE
set_flag(1, 4)
set_flag(1, 4)
click(8, 8)
click(0, 5) 
show_grid()
