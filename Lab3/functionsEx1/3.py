def solve(numheads, numlegs):
    y = int((numlegs - 2 * numheads) / 2)
    x = int(numheads - y)
    return x, y

numheads = 35
numlegs = 94
print(solve(numheads, numlegs))
