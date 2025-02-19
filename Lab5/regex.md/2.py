#program that matches a string that has an 'a' followed by two to three 'b'

import re #библиотека с регулярными выражениями

def ll(s):   #вызов функции
    return bool(re.fullmatch(r"a*bb{2,3}", s))
   
    """
    a* означает "ноль или более букв 'a'".
    bb{2,3} означает "две-три букв 'b'"
    bool преобразует результат в тру или фолс
    re.fullmatch(r"a*b*", s) —  проверяет, соответствует ли вся строка заданному шаблону
    """

s = input()   #запрашивает ввод
print(f"'{s}': {ll(s)}")  #вывод