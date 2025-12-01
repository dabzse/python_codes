"""Solve the eight queens problem."""
def parse_position(pos_str):
    """Parse algebraic position (e.g. e4) -> (col, row) 1..8 range."""
    s = pos_str.strip().lower().replace(',', ' ').split()
    if len(s) == 1:
        token = s[0]
        if len(token) == 2 and token[0].isalpha() and token[1].isdigit():
            col = ord(token[0]) - ord('a') + 1
            row = int(token[1])
            if 1 <= row <= 8 and 1 <= col <= 8:
                return row, col
        raise ValueError("Invalid position format. Examples: e4 or 4 5 (row col).")
    elif len(s) == 2:
        a, b = s
        if a.isdigit() and b.isdigit():
            row, col = int(a), int(b)
            if 1 <= row <= 8 and 1 <= col <= 8:
                return row, col
        raise ValueError("Invalid row and column numbers, must be 1..8.")
    else:
        raise ValueError("Invalid position format. Examples: e4 or 4 5 (row col).")


def solve_with_fixed(first_row, first_col):
    """Solve the eight queens problem with a fixed first queen position."""
    N = 8
    cols = [0] * (N + 1)
    used_col = [False] * (N + 1)
    used_diag1 = [False] * (2*N + 2)
    used_diag2 = [False] * (2*N + 2)
    solutions = []

    cols[first_row] = first_col
    used_col[first_col] = True
    used_diag1[first_row + first_col] = True
    used_diag2[first_row - first_col + N] = True

    def backtrack(row):
        if row > N:
            solutions.append(cols[1:].copy())
            return
        if row == first_row:
            backtrack(row + 1)
            return
        for c in range(1, N + 1):
            if not used_col[c] and not used_diag1[row + c] and not used_diag2[row - c + N]:
                used_col[c] = True
                used_diag1[row + c] = True
                used_diag2[row - c + N] = True
                cols[row] = c
                backtrack(row + 1)
                used_col[c] = False
                used_diag1[row + c] = False
                used_diag2[row - c + N] = False
                cols[row] = 0

    backtrack(1)
    return solutions


def render_board(cols):
    """ASCII chess board with queens."""
    out_lines = []
    out_lines.append("  +------------------------+")
    for r in range(8, 0, -1):
        line = f"{r} |"
        for f_idx in range(1, 9):
            is_light = ((r + f_idx) % 2 == 0)
            q_here = (cols[r-1] == f_idx)
            if q_here:
                cell = " ♛ "
            else:
                cell = " ◻ " if is_light else " ◼ "
            line += cell
        line += "|"
        out_lines.append(line)
    out_lines.append("  +------------------------+")
    out_lines.append("    a  b  c  d  e  f  g  h")
    return "\n".join(out_lines)


def solution_to_algebraic(cols):
    """Convert solution to algebraic notation, comma separated."""
    result = []
    for row in range(1, 9):
        col = cols[row-1]
        file_letter = chr(ord('a') + col - 1)
        result.append(f"{file_letter}{row}")
    return ", ".join(result)


def run_cli():
    """Main program, CLI version."""
    print("8 Queens Solver — give the position of the first queen.")
    print("Format: e4 or 4 5 (row col).")

    s = input("Enter the position of the first queen: ").strip()
    try:
        row, col = parse_position(s)
    except ValueError as e:
        print("Error:", e)
        return

    sols = solve_with_fixed(row, col)
    if not sols:
        print(f"No solution found with the first queen at {chr(ord('a')+col-1)}{row}.")
        return

    print(f"\nFound {len(sols)} solutions. Press enter for the next solution, q to quit.")
    idx = 0

    while True:
        print(f"\nSolution {idx+1}/{len(sols)} (first queen: {chr(ord('a')+col-1)}{row})")
        print(render_board(sols[idx]))
        print("\nNext solution:", solution_to_algebraic(sols[idx]))

        cmd = input("\nEnter = next solution, q = quit: ").strip().lower()
        if cmd == 'q':
            break
        idx += 1
        if idx >= len(sols):
            print("\nNo more solutions found.")
            break

if __name__ == "__main__":
    run_cli()
