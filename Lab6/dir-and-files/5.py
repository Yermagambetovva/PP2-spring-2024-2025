#program to write a list to a file.

import os

my_list = ["apple", "banana", "cherry"]

f = open("demofile2.txt", "a")
f.write(str(my_list))
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())