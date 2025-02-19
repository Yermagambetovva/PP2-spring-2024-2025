#program to replace all occurrences of space, comma, or dot with a colon.

import re  

# '[ ,.]' - шаблон для поиска пробела, запятой или точки
# ' ' - пробел
# ',' - запятая
# '.' - точка

text = input()  

pattern = '[ ,.]'   # шабло

# заменяем все пробелы, запятые и точки на двоеточие
replaced_text = re.sub(pattern, ':', text)

print(replaced_text)  
