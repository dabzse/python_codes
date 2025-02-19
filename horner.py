def horner(coeffs, x):
    """
    Horner-módszer polinomérték kiszámítására.

    :param coeffs: A polinom együtthatóinak listája (csökkenő hatványrendben).
    :param x: Az x érték, amelyre a polinomot ki kell értékelni.
    :return: A polinom értéke az adott x-nél.
    """
    result = 0
    for coeff in coeffs:
        result = result * x + coeff
    return result

# Példa: P(x) = 2x³ - 6x² + 2x - 1 kiértékelése x=3-nál
coefficients = [2, -6, 2, -1]  # 2x³ - 6x² + 2x - 1
x_value = 3
print(horner(coefficients, x_value))  # Kimenet: 5

# Példa: P(x) = 5x⁴ + 2x³ - 6x² - 3x + 20 kiértékelése x=4-nél
coefficients = [5, 2, -6, -3, 20]  # 5x⁴ + 2x³ - 6x² - 3x + 20
x_value = 4
print(horner(coefficients, x_value))  # Kimenet: 1320
