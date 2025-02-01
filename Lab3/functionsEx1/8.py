def spy_game(nums):
    c = [0, 0, 7]  #posledovatelnost kotoryu nado naiti
    c_index = 0    #index current num v c

    for num in nums:
        if num == c[c_index]:  #if number sovpadaet c current number v c
            code_index += 1          #perehodit k sled number
        if code_index == len(c):  #esli vse naideno
            return True

    return False  #esli ne naideno

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  #True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  #True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  #False
