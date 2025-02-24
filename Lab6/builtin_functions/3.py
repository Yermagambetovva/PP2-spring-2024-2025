#program with builtin function that checks whether a passed string is palindrome or not.

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

string = str(input())
print(is_palindrome(string))