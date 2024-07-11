# máximo de 3 letras consecutivas
# máximo 3999 mínimo 1
# I, V, X, L, C, D, M

# def normal_para_romanos(num: int) -> str: estava dando erro, e tive que criar uma lista para final, pois não imprimia
# os algarismos combinados, apenas os últimos.

# update 2024-07-11: ainda não funciona plenamente
def normal_para_romanos(num: int) -> None:

    final = []
    #2733
    qm = num // 1000
    dm = num % 1000
    final += qm * "M"
    if dm == 900:
        final = "CM"
        dm = 0

    qd = dm // 500
    dd = dm % 500
    final += qd * "D"
    if dd == 400:
        final += "CD"
        dd = 0

    qc = dd // 100
    dc = dd % 100
    final += qc * "C"
    if dc == 90:
        final += "XC"
        dc = 0

    ql = dc // 50
    dl = dc % 50
    final += ql * "L"
    if dl == 40:
        final += "XL"
        dl = 0

    qx = dl // 10
    dx = dl % 10
    final += qx * "X"
    if dx == 9:
        final += "IX"
        dx = 0

    qv = dx // 5
    dv = dx % 5
    final += qv * "V"
    if dv == 4:
        final += "IV"
        dv = 0

    qi = dv // 1
    di = dv % 1
    final += qi * "I"
    if di == 0:
        final += ""

    print(final)


normal_para_romanos(2733)