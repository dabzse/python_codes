def horner(coeffs, x):
    """
    Horner-módszer polinom értékének kiszámítására.

    :param coeffs: A polinom együtthatóinak listája (csökkenő hatványrendben).
    :param x: Az x érték, amelyre a polinomot ki kell értékelni.
    :return: A polinom értéke az adott x-nél.
    """
    result = 0
    for coeff in coeffs:
        result = result * x + coeff
    return result

# Felhasználói input bekérése
coefficients = list(map(float, input("Add meg a polinom együtthatóit szóközzel elválasztva (csökkenő hatványrendben): ").split()))
x_value = float(input("Add meg az x értékét: "))

# Polinom kiértékelése
result = horner(coefficients, x_value)
print(f"P({x_value}) = {result}")
