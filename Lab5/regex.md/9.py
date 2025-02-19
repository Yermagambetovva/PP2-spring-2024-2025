#program to insert spaces between words starting with capital letters.

import re  

# вводим строку в CamelCase
x = input()  

# '(?<=[a-z])([A-Z])' - шаблон для добавления пробела перед заглавной буквой
# '(?<=[a-z])' - смотрим, чтобы перед заглавной буквой была строчная буква (lookbehind)
# '([A-Z])' - находим заглавную букву, которую будем заменять

pattern = re.compile(r'(?<=[a-z])([A-Z])')  

# добавляем пробел перед заглавными буквами, сохраняя их
space = re.sub(pattern, r' \1', x)

print(space)  

