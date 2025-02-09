def generate_squares(N):
    for i in range(N + 1):
        yield i ** 2

N = int(input())

# Использование генератора
for square in generate_squares(N):
    print(square)
