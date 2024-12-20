import os
import sys


def exit_program(grid, value, row, col):
    grid[row][col] = int(value)
    display_grid(grid)
    print("This puzzle is not solvable")
    exit(1)
    

def display_grid(grid, input=False):
    # clears the terminal according to the right os command
    os.system('cts' if os.name == 'nt' else 'clear')
    
    if input:
        print("Input your Sudoku. Fill with numbers 1-9, or press Enter to leave cell blank")
        
    # prints the grid joined with spaces, replacing 0s with .
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
        
def input_puzzle():
    # initializes a 9x9 grid filled with 0s
    grid = [[0 for _ in range(9)] for _ in range(9)]
    
    # goes through each cell, updates the grid, the asks the user for the cell input
    for row in range(9):
        for col in range(9):
            display_grid(grid, True)
            value = input(f"Enter value for cell ({row+1}, {col+1}): ").strip()
            
            # check if the input is valid. If so, update grid, else keep it as 0
            
            if value.isdigit() and 1 <= int(value) <= 9:
                if not is_valid(grid, int(value), row, col):
                    exit_program(grid, value, row, col)
                grid[row][col] = int(value)

            
    # after final cell, displays grid   
    display_grid(grid)
    input("\nPress Enter to solve")
    return grid

def empty_space_finder(puzzle) :
    # iterates through all cells and, if it is empty, returns index
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r,c
    
    return None, None

def is_valid(puzzle, number, row, col):
    # this function checks if number is possible based on the row, column, and 3x3 grid (sudoku rules)
    
    # 1. Check row
    if number in puzzle[row]:
        return False
        
    # 2. Check column
    if number in (puzzle[i][col] for i in range(9)):
        return False
    
    # 3. Check grid
    row_start, col_start = (row // 3) * 3, (col // 3) * 3
    
    for i in range(row_start, row_start + 3):
        for j in range(col_start, col_start + 3):
            if puzzle[i][j] == number:
                return False
            
    # if all checks pass, then
    return True

def options_list_creator(puzzle, row, col):
   
    list_of_possible_vals = []
    
    # goes through every number 1-9 and passes it to is_valid
    for number in range(1,10):
        if is_valid(puzzle, number, row, col):
            list_of_possible_vals.append(number)
            
    return list_of_possible_vals
        
def recursive_solve(puzzle): 
    """
    Solve the Sudoku puzzle using backtracking.
    Returns True if a solution is found, otherwise False.
    """
    
    # finds the next empty square
    empty_index = empty_space_finder(puzzle)
    # checks if puzzle is completed
    if empty_index == (None, None):
        return True
    
    row_idx, col_idx = empty_index
    
    # create the list of possible values for that square
    options_list = options_list_creator(puzzle, row_idx, col_idx)

    # tries every possible option in option list
    for option in options_list:
        puzzle[row_idx][col_idx] = option
        display_grid(puzzle) 
        
        # checks if the puzzle is complete
        if recursive_solve(puzzle):
            return True
    
    # after loop, sets current square to 0
    # this means something before was wrong and has to backtrack
    puzzle[row_idx][col_idx] = 0
    
    # if no solution is found, puzzle is unsolvable
    return False

def main():
    puzzle = input_puzzle()
    solvable = recursive_solve(puzzle)
    
    if solvable:
        display_grid(puzzle)
        print("\nSolved Sudoku!")
    
    else:
        print("\nNo solution exists for the given Sudoku.")
        
if __name__ == '__main__':
    main()
    