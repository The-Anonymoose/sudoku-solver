# Sudoku Solver

    This project is a simple python script that recursively brute-forces Sudoku using a backtracking algorithm. The user is prompted to input a Sudoku puzzle and then the script attempts to solve it using a backtracking approach. The solution, if found, is displayed, and the user can see the solved grid.

## Code Structure
    - exit_program(grid, value, row, col): Ends the program when an invalid input is detected.
    - display_grid(grid, input=False): Displays the current Sudoku grid. If input=True, a prompt will ask the user to input their puzzle.
    - input_puzzle(): Prompts the user for the input grid and validates each entry.
    - empty_space_finder(puzzle): Searches for the next empty space in the grid.
    - is_valid(puzzle, number, row, col): Checks whether placing a number in a given cell adheres to Sudoku rules.
    - options_list_creator(puzzle, row, col): Generates a list of valid numbers that can be placed in an empty cell.
    - recursive_solve(puzzle): Attempts to solve the puzzle using the backtracking algorithm.
    - main(): The main driver function that runs the script, gets user input, and displays the result.