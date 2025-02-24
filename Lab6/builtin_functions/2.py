#program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

string = str(input())
result = count_case(string)
print(result)