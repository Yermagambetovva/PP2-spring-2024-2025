def reverse(s):
    return ' '.join(s.split()[::-1])  

user_input = input()  # 'str()' не нужен, так как input() уже возвращает строку
reversed_s = reverse(user_input)  
print(reversed_s)
