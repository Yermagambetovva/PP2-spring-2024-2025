#program to count the number of lines in a text 

with open("demofile.txt", "r") as file:
    len_count = sum(1 for line in file)

print(len_count)