#program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

import string

for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").close()
