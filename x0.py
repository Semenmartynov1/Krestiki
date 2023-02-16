def privet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x это номер строки  ")
    print(" y это номер столбца ")

def tabl():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(field):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

def vvod():
    while True:
        cords = input("    Ваш ход: ").split()

        if len(cords) != 2:
            print("Нужны две координаты ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа от 0 до 2 ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Введите числа от одного до двух! ")
            continue

        if field[x][y] != " ":
            print(" Занято! ")
            continue

        return x, y

def win_comb():
    wincord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in wincord:
        simvol = []
        for c in cord:
            simvol.append(field[c[0]][c[1]])
        if simvol == ["X", "X", "X"]:
            print("Выиграл X!")
            return True
        if simvol == ["0", "0", "0"]:
            print("Выиграл 0!")
            return True
    return False

privet()
field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    tabl()
    if count % 2 == 1:
        print(" Ходит крестик!")
    else:
        print(" Ходит нолик!")

    x, y = vvod()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if win_comb():
        break

    if count == 9:
        print(" Ничья!")
        break