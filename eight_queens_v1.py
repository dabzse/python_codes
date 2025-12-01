def solve_eight_queens():
    """
    CLI program to solve the Eight Queens puzzle with a user-specified
    starting position for the first queen.
    """
    print("This program solves the Eight Queens puzzle. You will enter a valid field (a1-h8) "
          "for the first queen, and the program will automatically find a solution for the rest.")

    while True:
        user_input = input("Enter a valid field for the first queen (e.g., 'a1', 'h8'): ").lower()
        if len(user_input) == 2 and 'a' <= user_input[0] <= 'h' and '1' <= user_input[1] <= '8':
            start_col = ord(user_input[0]) - ord('a')
            start_row = int(user_input[1]) - 1
            break
        else:
            print("Invalid input. Please enter a field like 'a1' or 'h8'.")

    n = 8
    board = [-1] * n  # board[i] will store the column of the queen in row i
    solutions_found = []

    def is_safe(current_row, current_col):
        """
        Checks if placing a queen at (current_row, current_col) is safe
        given queens in previous rows.
        """
        for prev_row in range(current_row):
            # Check for column conflict or diagonal conflict
            if (board[prev_row] == current_col or
                    abs(board[prev_row] - current_col) == abs(prev_row - current_row)):
                return False
        return True

    def solve(row):
        """
        Recursive backtracking function to place queens.
        """
        if row == n:
            solutions_found.append(list(board))
            return True  # Found one solution

        if row == start_row:
            # If this is the starting row, place the queen at start_col
            board[row] = start_col
            if is_safe(row, start_col):
                if solve(row + 1):
                    return True
            board[row] = -1  # Backtrack
            return False # If the initial placement leads to no solution, no other options for this row
        else:
            # For other rows, try all columns
            for col in range(n):
                board[row] = col
                if is_safe(row, col):
                    if solve(row + 1):
                        return True
                board[row] = -1  # Backtrack
        return False

    def print_board(solution):
        """
        Prints the chessboard for a given solution.
        """
        print("\nSolution found:")
        print("  " + " ".join([chr(ord('a') + i) for i in range(n)]))
        print("  " + "--" * n)
        for r in range(n):
            row_str = f"{r + 1}|"
            for c in range(n):
                if solution[r] == c:
                    row_str += "Q "
                else:
                    row_str += ". "
            print(row_str)
        print()

    # Initialize board with the first queen's position
    # The `solve` function will handle placing the first queen if `row == start_row`
    # We start the solve from row 0, and it will jump to `start_row`'s logic when it reaches it.
    if solve(0):
        print_board(solutions_found[0])
    else:
        print(f"\nNo solution found with the first queen at {user_input}.")

if __name__ == "__main__":
    solve_eight_queens()
    def print_board(solution):
        """
        Prints the chessboard for a given solution, with a1 at the bottom-left.
        """
        print("\nSolution found:")
        print("  " + " ".join([chr(ord('a') + i) for i in range(n)]))
        print("  " + "--" * n)
        for r in range(n - 1, -1, -1):  # Iterate from n-1 down to 0
            row_str = f"{r + 1}|"
            for c in range(n):
                if solution[r] == c:
                    row_str += "Q "
                else:
                    row_str += ". "
            print(row_str)
        print()
