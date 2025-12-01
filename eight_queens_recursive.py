def parse_position(pos):
    """Parse algebraic position (e.g. e4) -> (row, col)."""
    if len(pos) != 2:
        return None
    file = pos[0].lower()
    rank = pos[1]

    if file < 'a' or file > 'h':
        return None
    if not rank.isdigit():
        return None

    row = int(rank) - 1
    col = ord(file) - ord('a')
    if row < 0 or row > 7:
        return None

    return row, col


def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe."""
    for r in range(row):
        c = board[r]
        if c == -1:
            continue
        if c == col:
            return False
        if abs(c - col) == abs(r - row):
            return False
    return True


def solve_recursive(row, board, solutions):
    """Recursive backtracking."""
    if row == 8:
        solutions.append(board.copy())
        return

    if board[row] != -1:
        # If this row is already occupied, skip it
        if is_safe(board, row, board[row]):
            solve_recursive(row + 1, board, solutions)
        return

    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col
            solve_recursive(row + 1, board, solutions)
            board[row] = -1  # backtracking


def render(board):
    """ASCII chessboard."""
    print("  +------------------------+")
    for r in range(7, -1, -1):
        line = f"{r+1} |"
        for c in range(8):
            if board[r] == c:
                line += " ♛ "
            else:
                line += (" ◻ " if (r + c) % 2 == 0 else " ◼ ")
        line += "|"
        print(line)
    print("  +------------------------+")
    print("    a  b  c  d  e  f  g  h")


def algebraic(board):
    """Convert solution to algebraic notation."""
    out = []
    for r in range(8):
        c = board[r]
        file = chr(ord('a') + c)
        rank = r + 1
        out.append(file + str(rank))
    return ", ".join(sorted(out))


# --- Main program ---

pos = input("Enter the position of the first queen (e.g. e4): ")
parsed = parse_position(pos)

if not parsed:
    print("Invalid position!")
    exit()

row, col = parsed

# -1 = empty row
board = [-1] * 8
board[row] = col  # first queen

solutions = []
solve_recursive(0, board, solutions)

if not solutions:
    print("No solution found with this first queen position.")
else:
    print("\nSolution found:")
    render(solutions[0])
    print("\nAlgebraic notation:")
    print(algebraic(solutions[0]))
