"""Крестики-нолики"""

table = list(range(1, 10))

"""
Функция создания поля игры
Пример пустого поля:
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
"""


def draw_board(table):  # рисуем поле
    for i in range(3):  # в нашем случае 3х3
        print("|", table[0 + i * 3], "|", table[1 + i * 3], "|", table[2 + i * 3], "|")


"""
Функция заполнения ячеек:
Пример пустого поля:
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

Пример поля с символами игроков:
    [[Х, 2, 3],
    [О, 5, Х],
    [7, О, 9]]
"""


def take_place_input(player_input):  # добавляем символ на поле
    valid = False
    while not valid:
        player_answer = input("В ячейку под каким номером поставить " + player_input + "? ")
        try:
            player_answer = int(player_answer)  # номер ячейки - целое число от 1 до 9
        except:
            print("Необходимо выбрать номер ячейки от 1 до 9")  # если ответ отличается, то выводим сообщение
            continue
        if 1 <= player_answer <= 9:  # если ответ лежит в пределах от 1 до 9
            if str(table[player_answer - 1]) not in "XO":  # и еще не занят ни одним из игроков
                table[player_answer - 1] = player_input  # то заполняем ячейку
                valid = True
            else:
                print("Эта клетка уже занята!")  # если ячейка занята, то выводим сообщение
        else:
            print("Введите число от 1 до 9")  # если число лежит за пределами [1,9]


"""Функция выигрыша
По логике игры побеждает тот игрок, который выстроил в ряд (по горизонтали, вертикали, диагонали) 
из трех ячеек символ, присвоенный ему"""


def who_win(table):
    win_places = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8),
                  (2, 4, 6)]  # комбинации выигрышей
    for (x, y, z) in win_places:
        if table[[x]] == table[y] == table[z] and (table[x] == "X" or table[x] == "O"):  # если символы приняли одну
            # из комбинаций, и ячейки не являются пустыми
            return table[x]
    return print("Игра продолжается")


"""
Процесс игры
"""


# noinspection PyArgumentList
def game(table):
    counter = 0  # считаем количество ходов
    win = False
    while not win:
        draw_board(table)  # рисуем поле
        if counter % 2 == 0:  # если количество ходов четное - ходит Х
            take_place_input("X")
        else:
            take_place_input("O")  # иначе - ходит О
        counter += 1
        if counter > 4:  # если количество ходов > 4 - минимальное количество, при котором
            # может выиграть один из игроков
            player_win = who_win(table)  # запускаем проверку победителя
            if player_win:
                print(player_win, "выиграл!")  # сообщение, если есть выигрышная комбинация
                win = True
                break
        if counter == 9:  # максимальное количество ходов
            print("Ничья!")  # если количество ходов равно 9, то ничья!
            break
    draw_board(table)


game(table)
