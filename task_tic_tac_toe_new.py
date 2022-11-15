from typing import List, Union, Tuple

"""
Функция создания поля

Пример путого поля 3x3 - | | | | 
                         | | | | 
                         | | | | 
                         
Пример заполненного поля - |X| | | 
                           | |O| | 
                           | | |X| 
"""


def get_table(size: int, empty_place: Union[str, None]) -> List[List]:
    """
    Возвращает пустое поле
    :param size: параметр размера поля
    :param empty_place: параметр заполнения пустой ячейки
    :return: поле в виде списка списков
    """
    table = []
    for _ in range(size):
        table.append([empty_place] * size)  # создаем список списков, умноженных на размер поля
    return table


def draw_table(table: List[List]) -> None:
    """
    Превращаем поле из списка списков в стандартное поле для игры
    :param table:
    :return:
    """
    for row in table:
        for cell in row:
            print(f"|{cell}", end="")
        print("|")


def get_int_val(text, border=None):
    """
    Возвращаем целое число с проверками
    :param text: вводимые параметры для постановки в ячейку поля
    :param border:
    :return:
    """
    while True:
        val = input(text)
        try:
            val = int(val)
        except ValueError:
            print("Должно быть целое число")
            continue
        if border is None:
            pass
        else:
            if not 0 <= val <= border:
                print(f"Значение должно быть в интервале (0, {border})\n")
                continue
        return val


def get_index_from_step(table: List[List], size: int) -> Tuple[int, int]:
    """
        Функция для получения координат ячейки
        :param table:
        :param size:
        :return:
        """
    while True:
        index_row = get_int_val("Введи индекс для строки, куда ставим символ\n", size - 1)
        index_col = get_int_val("Введи индекс для столбца, куда ставим символ\n", size - 1)
        if table[index_row][index_col] != " ":
            print("Ячейка занята")
            continue
        return index_row, index_col


def set_on_place(table, current_player, index_row, index_col):
    """
    Функция постановки символа игрока в ячейку
    :param table:
    :param current_player: текущий игрок
    :param index_row: параметр строки
    :param index_col: параметр столбца
    :return:
    """
    table[index_row][index_col] = current_player
    return table


def change_player(player):
    """
    Функция смены игрока относительно текущего
    :param player: игрок, которого заменяем
    :return: возвращаем игрока с другим символом
    """
    if player == "X":
        new_player = "O"
    else:
        new_player = "X"
    return new_player


def win_game(table):
    """
    Функция проверки выигрыша
    :param table:
    :return:
    """
    for win_combination in table:
        if win_combination in "|X|X|X|":
            print('Выиграл игрок, который ходил Х')
        elif win_combination in "|O|O|O|":
            print('Выиграл игрок, который ходил O')
        else:
            print('Продолжаем игру')


"""
Функция запуска игры
"""


def game(table, size, player):
    current_player = player  # текущий игрок
    counter = 0  # счетчик ходов
    draw_table(table)  # отрисовываем поле
    while counter < size * size:  # пока количество ходов не превышает макс. значение (поле 3х3 = 9 ходов, 4х4 = 16)
        print(f"Ставит игрок {current_player}")
        index_row, index_col = get_index_from_step(table, size)  # получили координаты для хода
        table = set_on_place(table, current_player, index_row, index_col)
        counter += 1  # обновление счетчика
        draw_table(table)  # отрисовываем поле
        if win_game(table):  # проверка выигрыша
            print(f'Выиграл игрок {current_player}')
            return current_player  # возвращаем текущего игрока
        current_player = change_player(current_player)  # смена игрока
    if counter == size * size:
        print("Ничья")
        print("Есть желание повторить игру? да/нет")
        continue_game = "да" or "нет"
        if continue_game == "да":
            game(table, size, player)
        else:
            print("Игра окончена.")


"""
Процесс игры
"""


def begin():
    global who_play
    size = get_int_val("Введи размер поля\n")
    empty_place = f'| |'  # пустые места заполняются числами от 1 до размера поля к квадрате
    table = get_table(size, empty_place)
    player = input("Кто ходит первый? X/O\n")  # кто ходит первый "X" или "O"
    if player == "X" or "O":
        who_play = input("С кем будет игра? Ч(человек)/К(компьютер)\n")
        if who_play == "человек" or "Ч":  # если "человек",
            game(table, size, player)  # то начинаем игру
        elif who_play == "компьютер" or "К":  # если "компьютер"
            print("В разработке")  # то выводим сообщение
            last_question = input("Есть желание сыграть с человеком?) да/нет\n")  # предлагаем выбрать человека
            if last_question == "да":  # если выбирает да
                game(table, size, player)  # то начинаем игру
            else:  # если вводится что-то другое
                print("Игра окончена")  # выводим сообщение


if __name__ == "__main__":
    begin()
