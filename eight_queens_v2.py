def parse_position(pos_str):
    s = pos_str.strip().lower().replace(',', ' ').split()
    if len(s) == 1:
        token = s[0]
        if len(token) == 2 and token[0].isalpha() and token[1].isdigit():
            col = ord(token[0]) - ord('a') + 1
            row = int(token[1])
            if 1 <= row <= 8 and 1 <= col <= 8:
                return row, col
        raise ValueError("Nem jó formátum. Példák: e4  vagy  4 5 (row col).")
    elif len(s) == 2:
        a, b = s
        if a.isdigit() and b.isdigit():
            row, col = int(a), int(b)
            if 1 <= row <= 8 and 1 <= col <= 8:
                return row, col
        raise ValueError("Sor és oszlop számként 1..8 értékekkel.")
    else:
        raise ValueError("Nem jó formátum. Példák: e4  vagy  4 5 (row col).")

def solve_with_fixed(first_row, first_col):
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
    out_lines = []
    out_lines.append("  +-------------------------------+")
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
    out_lines.append("  +-------------------------------+")
    out_lines.append("    a  b  c  d  e  f  g  h")
    return "\n".join(out_lines)

def solution_to_algebraic(cols):
    result = []
    for row in range(1, 9):
        col = cols[row-1]
        file_letter = chr(ord('a') + col - 1)
        result.append(f"{file_letter}{row}")
    return ", ".join(result)

def run_cli():
    print("8-királynő — megadod az első királynő helyét, a program beállítja a többit.")
    print("Formátumok elfogadva: e4  vagy  4 5   (sor 1..8, oszlop 1..8).")

    s = input("Add meg az első királynő helyét: ").strip()
    try:
        row, col = parse_position(s)
    except ValueError as e:
        print("Hiba:", e)
        return

    sols = solve_with_fixed(row, col)
    if not sols:
        print(f"Nincs megoldás a {row},{col} (vagy {chr(ord('a')+col-1)}{row}) első királynővel.")
        return

    print(f"\nTalált {len(sols)} megoldást. Megjelenítjük sorban — Enter következő, q kilép.")
    idx = 0

    while True:
        print(f"\nMegoldás {idx+1}/{len(sols)} (az első királynő: {chr(ord('a')+col-1)}{row})")
        print(render_board(sols[idx]))
        print("\nLehetséges megoldás:", solution_to_algebraic(sols[idx]))

        cmd = input("\nEnter = következő, q = kilép: ").strip().lower()
        if cmd == 'q':
            break
        idx += 1
        if idx >= len(sols):
            print("\nVége — nincs több megoldás.")
            break

if __name__ == "__main__":
    run_cli()
