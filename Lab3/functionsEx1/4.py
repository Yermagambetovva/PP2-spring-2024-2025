def is_prime(n):  #проверяет является ли число n простым
    return n > 1 and all(n % i != 0 for i in range(2, n))  #проверяет, не делится ли n на числа от 2 до n-1.Если не делится ни на одно, значит число простое.

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)] #Если число простое, оно добавляется в новый список. Возвращает новый список с простыми числами.

input_numbers = list(map(int, input().split()))
print(filter_prime(input_numbers))
