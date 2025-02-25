#program to copy the contents of a file to another file

with open("demofile.txt", "r") as g, open("demofile2.txt", "a") as f:
    f.write(g.read())

with open("demofile2.txt", "r") as f:
    print(f.read())
