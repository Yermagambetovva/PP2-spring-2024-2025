#program to split a string at uppercase letters.

import re  

# вводим строку, где слова слиты в CamelCase
x = input()  

# '[A-Z][^A-Z]*' - шаблон для разделения слов в CamelCase
# '[A-Z]' - ищем заглавную букву (начало нового слова)
# '[^A-Z]*' - далее идут любые символы, кроме заглавных букв (остальная часть слова)

pattern = r'[A-Z][^A-Z]*'  

# находим все слова, соответствующие шаблону
split_strings = re.findall(pattern, x)

# объединяем найденные слова через пробел
print(' '.join(split_strings))  
