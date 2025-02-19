#program to convert snake case string to camel case string.

import re  

# вводим строку в snake_case
snake = input()  

# '(_\w)' - шаблон для поиска подчеркивания и следующей буквы
# '_' - подчеркивание
# '\w' - любая буква, цифра или символ подчеркивания

pattern = re.compile(r'(_\w)')  

# заменяем '_буква' на 'Буква' (удаляем подчеркивание и делаем букву заглавной)
camel = re.sub(pattern, lambda x: x.group(1)[1:].upper(), snake)

print(camel)  
