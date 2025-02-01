from itertools import permutations

def print_permutations(string):
    p = permutations(string)
    for perm in p:   #perm eto kortezh ('a', 'b', 'c')
        print(''.join(perm)) #preobrazuet kortezh

user_input = str(input())
print_permutations(user_input)
