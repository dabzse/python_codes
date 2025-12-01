# Parse algebraic position (e.g. e4) -> (col, row) in range 1..8
def parse_position(pos):
    """Parse algebraic position (e.g. e4) -> (col, row) in range 1..8"""
    pos = pos.strip().lower()
    if len(pos) != 2:
        return None
    file = pos[0]
    rank = pos[1]
    if file < 'a' or file > 'h':
        return None
    if not rank.isdigit():
        return None
    row = int(rank)
    if row < 1 or row > 8:
        return None
    col = ord(file) - ord('a') + 1
    return (col, row)


# Check if a queen at (row, col) is safe given a solution
def is_safe(col, row, solution):
    """
    Check if a queen at (row, col) is safe given a solution.
    """
    for r in range(1, 9):
        c = solution[r]
        if c == 0:
            continue
        if r == row:
            continue
        # same column
        if c == col:
            return False
        # diagonals
        if abs(c - col) == abs(r - row):
            return False
    return True


# Backtracking: try to place queens in each row (1..8)
def solve_from_row(row, solution, solutions):
    """Backtracking: try to place queens in each row (1..8)"""
    if row == 9:
        # full solution
        solutions.append(solution.copy())
        return

    # if the row is already occupied by the user, check if it is safe
    if solution[row] != 0:
        if is_safe(solution[row], row, solution):
            solve_from_row(row + 1, solution, solutions)
        return

    # try all columns
    for col in range(1, 9):
        if is_safe(col, row, solution):
            solution[row] = col
            solve_from_row(row + 1, solution, solutions)
            solution[row] = 0  # backtrack


def render_board(cols):
    """ASCII chessboard with solutions"""
    print("  +------------------------+")
    for row in range(8, 0, -1):
        line = f"{row} |"
        for col in range(1, 9):
            if cols[row] == col:
                line += " ♛ "
            else:
                line += " ◻ " if (row + col) % 2 == 0 else " ◼ "
        line += "|"
        print(line)
    print("  +------------------------+")
    print("    a  b  c  d  e  f  g  h")


# Convert a solution to algebraic notation
def solution_to_algebraic(cols):
    """Convert a solution to algebraic notation"""
    pairs = []
    for row in range(1, 9):
        col = cols[row]
        if col == 0:
            continue
        file_letter = chr(ord('a') + col - 1)
        pairs.append((file_letter, row))
    pairs.sort(key=lambda x: (x[0], x[1]))
    return ", ".join(f"{f}{r}" for f, r in pairs)


# --- Main program ---
first = input("Enter the position of the first queen (e.g. e4): ").strip()
parsed = parse_position(first)
if not parsed:
    print("Invalid position!")
    exit()

first_col, first_row = parsed

# solution: 1..8 keys, 0 = empty, 1..8 = column
solution = {i: 0 for i in range(1, 9)}
solution[first_row] = first_col

solutions = []
solve_from_row(1, solution, solutions)

if not solutions:
    print("No solution found with this first queen position.")
    exit()

sol = solutions[0]
print("\nSolution in ASCII chessboard:")
render_board(sol)
print("\nSolution in algebraic notation:")
print(solution_to_algebraic(sol))
