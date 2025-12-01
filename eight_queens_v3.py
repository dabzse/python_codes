# Javított 8-királynő (1..8 indexelés használatban)
# A fő javítás: is_safe most már az összes beállított sort ellenőrzi,
# így a felhasználó által előre megadott későbbi sorok is figyelembe vannak véve.

def parse_position(pos):
    """Algebrai pozíció (pl. e4) -> (col, row) 1..8 tartományban."""
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


def is_safe(col, row, solution):
    """
    Ellenőrzi, hogy (row,col) nem ütközik-e egy már elhelyezett királynővel.
    Megvizsgál *minden* sort, ahol solution[r] != 0 (üres = 0).
    """
    for r in range(1, 9):
        c = solution[r]
        if c == 0:
            continue
        if r == row:
            continue
        # azonos oszlop
        if c == col:
            return False
        # átlók
        if abs(c - col) == abs(r - row):
            return False
    return True


def solve_from_row(row, solution, solutions):
    """Backtracking: soronként próbálunk királynőket elhelyezni (1..8)."""
    if row == 9:
        # teljes megoldás
        solutions.append(solution.copy())
        return

    # Ha a sor már előre be van állítva (felhasználó), ellenőrizzük, hogy biztonságos-e
    if solution[row] != 0:
        if is_safe(solution[row], row, solution):
            solve_from_row(row + 1, solution, solutions)
        return

    # különben próbáljuk az összes oszlopot
    for col in range(1, 9):
        if is_safe(col, row, solution):
            solution[row] = col
            solve_from_row(row + 1, solution, solutions)
            solution[row] = 0  # visszalépés


def render_board(cols):
    """ASCII sakktábla világos szemszögből. cols: dict/list 1..8 -> colNumber."""
    print("  +-------------------------------+")
    for row in range(8, 0, -1):
        line = f"{row} |"
        for col in range(1, 9):
            if cols[row] == col:
                line += " ♛ "
            else:
                line += " ◻ " if (row + col) % 2 == 0 else " ◼ "
        line += "|"
        print(line)
    print("  +-------------------------------+")
    print("    a  b  c  d  e  f  g  h")


def solution_to_algebraic(cols):
    """Visszaadja a pozíciókat algebrai jelöléssel, betű szerint rendezve."""
    pairs = []
    for row in range(1, 9):
        col = cols[row]
        if col == 0:
            continue
        file_letter = chr(ord('a') + col - 1)
        pairs.append((file_letter, row))
    pairs.sort(key=lambda x: (x[0], x[1]))
    return ", ".join(f"{f}{r}" for f, r in pairs)


# --- Fő program ---
first = input("Add meg az első királynő helyét (pl. e4): ").strip()
parsed = parse_position(first)
if not parsed:
    print("Hibás formátum!")
    exit()

first_col, first_row = parsed

# solution: 1..8 kulcsok, 0 = üres, 1..8 = oszlop
solution = {i: 0 for i in range(1, 9)}
solution[first_row] = first_col

solutions = []
solve_from_row(1, solution, solutions)

if not solutions:
    print("Ehhez a kezdőpozícióhoz nincs megoldás.")
    exit()

sol = solutions[0]
print("\nMegoldás sakktáblán:")
render_board(sol)
print("\nAlgebrai jelöléssel (betű szerint):")
print(solution_to_algebraic(sol))
