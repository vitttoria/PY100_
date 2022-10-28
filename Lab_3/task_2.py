my_dict = {}


def get_count_char(str_):
    str_ = ''.join(str_.lower().split())
    for sym in str_:
        sym_count = str_.count(sym)
        if sym_count > 1:
            my_dict[sym] = sym_count
    return my_dict


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
