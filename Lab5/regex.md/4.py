#program to find the sequences of one upper case letter followed by lower case letters

import re  

# '\b' - граница слова (начал или конец слова)
# '[A-Z]' - первая буква должна быть заглавной (от A до Z)
# '[a-z]+' - далее должны следовать строчные буквы (от a до z), минимум одна
# '\b' - конец слова

pattern = r'\b[A-Z][a-z]+\b'

x = input()  #ввод

#ищем все совпадения в строке по заданному шаблону
matches = re.findall(pattern, x)

print(matches)  # Вывод