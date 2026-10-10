"""
EN:
    Given a 4-digit sequence with no duplicate digits.
    The clues are provided.
    The task: guess the number.
    Each clue consists of a 4-digit number and a pattern.
    "."         means that the digit is in the number and in the correct position.
    "+"         means that the digit is in the number, but in the wrong position.
    "-" and "0" mean that the digit is not in the number.

for instanse
    "1 2 3 4 ."                 means 1 digit is in the number and in the correct position.
    "1 2 3 4 .+"                means 2 digits are in the number: one in the correct position, the other in the wrong position.
    "1 2 3 4 +++"               means 3 digits are in the number, but all in the wrong position.
    "1 2 3 4 0" and "1 2 3 4 -" mean none of the digits are in the number.

when you are done, type "end".

----------------

HU:
    Adott egy 4 jegyű, ismétlődésmentes számsor.
    A feltételeket megadják.
    A feladat: kitalálni a számot.

    Minden feltétel egy 4-jegyű szám és egy minta megadása.
    "."         Azt jelenti, hogy a szám benne van és jó helyen van.
    "+"         Azt jelenti, hogy a szám benne van, de rossz helyen van.
    "-" és "0"  Azt jelenti, hogy a szám nincs benne.

például
    "1 2 3 4 ."                 Azt jelenti, hogy 1 szám benne van és jó helyen van.
    "1 2 3 4 .+"                Azt jelenti, hogy 2 szám benne van, egyik jó helyen, a másik rossz helyen.
    "1 2 3 4 +++"               Azt jelenti, hogy 3 szám benne van, de mind rossz helyen van.
    "1 2 3 4 0" és "1 2 3 4 -"  Azt jelenti, hogy egyik szám sincs benne.

ha végeztél, írd be: "end".
"""
import itertools


def parse_line(line):
    tokens = line.strip().split()
    if len(tokens) < 5:
        return None, "Kérlek add meg a 4 számot és a patternt szóközökkel elválasztva (pl. 1 2 3 4 +)!"

    numbers = tokens[:4]
    pattern = "".join(tokens[4:])

    if len(set(numbers)) != 4:
        return None, "Egy tippen belül nem lehet számismétlés (mind a 4 számnak különbözőnek kell lennie)!"

    valid_chars = set("+.-0")
    if not set(pattern).issubset(valid_chars):
        return None, f"A minta csak '+', '-', '.' vagy '0' karaktereket tartalmazhat! (Megadott: '{pattern}')"

    exp_dots = pattern.count('.')   # jó helyen (.)
    exp_plus = pattern.count('+')   # van benne, de rossz helyen (+)

    if exp_dots + exp_plus > 4:
        return None, "A helyes számok összege legfeljebb 4 lehet egy tippen belül!"

    return (numbers, exp_dots, exp_plus), None


def collect_clues():
    """Begyűjti a feltételeket a konzolról."""
    clues = []
    entered_numbers = set()

    while True:
        try:
            line = input("Feltétel > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nKilépés...")
            return None, None

        if not line:
            continue

        if line.lower() == "end":
            if not clues:
                print("Még nem adtál meg egyetlen feltételt sem!")
                continue
            break

        parsed, error_msg = parse_line(line)
        if error_msg:
            print(f"  [!] Hiba: {error_msg}")
            continue

        clues.append(parsed)
        entered_numbers.update(parsed[0])
        print(f"  -> {len(clues)}. feltétel rögzítve.")

    return clues, entered_numbers


def check_candidate(candidate, clues):
    """Megvizsgálja, hogy egy adott 4-es számsor teljesíti-e az összes feltételt."""
    for guess, exp_dots, exp_plus in clues:
        actual_dots = sum(1 for i in range(4) if guess[i] == candidate[i])
        actual_plus = sum(1 for i in range(4) if guess[i] in candidate and guess[i] != candidate[i])

        if actual_dots != exp_dots or actual_plus != exp_plus:
            return False
    return True


def display_results(solutions):
    """Megjeleníti a végeredményt."""
    print("=" * 60)
    if not solutions:
        print("Nincs olyan kombináció, amely minden megadott feltételnek megfelelne!")
    elif len(solutions) == 1:
        print("Megtalált megoldás:")
        print("  " + " ".join(solutions[0]))
    else:
        print(f"Több lehetséges megoldás van ({len(solutions)} db):")
        for sol in solutions:
            print("  " + " ".join(sol))
    print("=" * 60)


def main():
    print("=" * 60)
    print("         SZÁMKITALÁLÓS JÁTÉK MEGFEJTŐ")
    print("=" * 60)
    print("Írd be a feltételeket soronként a következő formátumban:")
    print("  <szám1> <szám2> <szám3> <szám4> <pattern>")
    print("\nPéldák:")
    print("  1 2 3 4 +       (1 szám benne van rossz helyen, a többi nincs)")
    print("  5 6 7 8 ++      (2 szám benne van rossz helyen, a többi nincs)")
    print("  9 0 1 2 ----    (egyik szám sincs benne, elég a '-' vagy '0' is)")
    print("  3 5 8 2 .       (1 szám jó helyen van benne)")
    print("\nHa beírtad az összes feltételt, írd be: end")
    print("-" * 60)

    clues, entered_numbers = collect_clues()
    if clues is None:
        return

    print("-" * 60)
    print("Számolás...")

    # Lehetséges számkészlet meghatározása (0-9 vagy a megadott számok)
    if all(n.isdigit() and 0 <= int(n) <= 9 for n in entered_numbers):
        pool = [str(i) for i in range(10)]
    else:
        pool = sorted(entered_numbers)

    # Permutációk szűrése
    solutions = [
        cand for cand in itertools.permutations(pool, 4)
        if check_candidate(cand, clues)
    ]

    display_results(solutions)


if __name__ == "__main__":
    main()
