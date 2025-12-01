def parse_position(pos):
    """Algebrai pozíciót (pl. e4) -> (sor, oszlop) alakít."""
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


def safe(board, row, col):
    """Ellenőrzi, hogy a (row, col) helyre tehető-e királynő."""
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
    """Rekurzív backtracking."""
    if row == 8:
        solutions.append(board.copy())
        return

    if board[row] != -1:
        # KELL safe ellenőrzés (javítás!)
        if safe(board, row, board[row]):
            solve_recursive(row + 1, board, solutions)
        return

    for col in range(8):
        if safe(board, row, col):
            board[row] = col
            solve_recursive(row + 1, board, solutions)
            board[row] = -1  # visszalépés


def render(board):
    """ASCII sakktábla világos nézetből."""
    print("  +-------------------------------+")
    for r in range(7, -1, -1):
        line = f"{r+1} |"
        for c in range(8):
            if board[r] == c:
                line += " ♛ "
            else:
                line += (" ◻ " if (r + c) % 2 == 0 else " ◼ ")
        line += "|"
        print(line)
    print("  +-------------------------------+")
    print("    a  b  c  d  e  f  g  h")


def algebraic(board):
    """Megoldás átalakítása rendezett algebrai listává."""
    out = []
    for r in range(8):
        c = board[r]
        file = chr(ord('a') + c)
        rank = r + 1
        out.append(file + str(rank))
    return ", ".join(sorted(out))


# --- Fő program ---

pos = input("Add meg az első királynő helyét (pl. e4): ")
parsed = parse_position(pos)

if not parsed:
    print("Hibás pozíció!")
    exit()

row, col = parsed

# -1 = üres sor
board = [-1] * 8
board[row] = col  # felhasználó első királynője

solutions = []
solve_recursive(0, board, solutions)

if not solutions:
    print("Nincs megoldás ezzel a kezdőpozícióval.")
else:
    print("\nMegoldás:")
    render(solutions[0])
    print("\nAlgebrai jelöléssel:")
    print(algebraic(solutions[0]))
