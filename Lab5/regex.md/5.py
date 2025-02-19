#program that matches a string that has an 'a' followed by anything, ending in 'b'

import re  

# '\b' - граница слова (начало или конец слова)
# '[A-Z]' - первая буква должна быть заглавной (от A до Z)
# '[a-z]+' - далее должны следовать строчные буквы (от a до z), минимум одна
# '\b' - конец словa

pattern = r'\b[A-Z][a-z]+\b'

x = input()  

# ищем все совпадения в строке по заданному шаблону
matches = re.findall(pattern, x)

print(matches)  