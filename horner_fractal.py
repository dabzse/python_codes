from decimal import Decimal
from fractions import Fraction

def horner(coeffs, x):
    result = Decimal(coeffs[0])  # Kezdő együttható
    for coef in coeffs[1:]:
        result = result * Decimal(x) + Decimal(coef)
    return result

# Kérjük a felhasználót, hogy adja meg az együtthatókat szóközökkel elválasztva
input_coeffs = input("Add meg az együtthatókat szóközökkel elválasztva: ")

# A bemeneti együtthatókat stringből listává alakítjuk
coeffs = []
for coef in input_coeffs.split():
    try:
        if '/' in coef:  # Ha törtet kapunk, Fraction-be alakítjuk
            coef_value = Fraction(coef)  # Tört számként értelmezzük
            coef_value = float(coef_value)  # Törtet float-tá alakítjuk
        else:
            coef_value = float(coef)  # Ha sima szám, akkor float
    except ValueError:
        print(f"Hiba történt az együttható '{coef}' feldolgozása közben.")
        exit(1)
    coeffs.append(coef_value)

# Kérjük a felhasználót, hogy adja meg az x értékét (tört alakban is)
x_input = input("Add meg az x értékét: ")

# Tört értékek kezelése: ha törtet adunk meg, pl. '7/13'
try:
    if '/' in x_input:
        x_value = Fraction(x_input)  # Ha törtet kapunk, Fraction-be alakítjuk
        x_value = float(x_value)  # Törtet float-tá alakítjuk
    else:
        x_value = Decimal(x_input)  # Ha sima szám, akkor Decimal
except Exception as e:
    print(f"Hiba történt az x értékének beolvasásakor: {e}")
    exit(1)

# Kiszámoljuk a polinom értékét
result = horner(coeffs, x_value)

# Eredmény kiírása, kerekítés nélkül
print(f"P({x_value}) = {result}")

# Eredmény kiírása, kerekítve két tizedesjegyre
result = result.quantize(Decimal('0.01'))  # Kerekítés két tizedesjegyre

print(f"P({x_value}) = {result} (kerekítve)")
