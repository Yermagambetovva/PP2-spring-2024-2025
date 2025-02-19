#program to convert a given camel case string to snake case

import re  

# вводим строку в CamelCase
camel = input()  

# '(?<!^)(?=[A-Z])' - шаблон для добавления подчеркивания перед заглавными буквами
# '(?<!^)' - исключаем первый символ (чтобы не добавлять подчеркивание в начале)
# '(?=[A-Z])' - перед каждой заглавной буквой добавляем подчеркивание

pattern = re.compile(r'(?<!^)(?=[A-Z])')  

# заменяем найденные места подчеркиванием и переводим в нижний регистр
snake = re.sub(pattern, '_', camel).lower()

print(snake)  
