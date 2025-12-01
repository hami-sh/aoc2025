
from io import open_code
from os import read


def sol():
    at_zero = 0
    pos = 50

    f = open("./day01/dummy.txt")
    for line in f.readlines():
        direction = line[0]
        length = int(line[1:-1])
        print(f"{direction} {length}")
        if direction == "L":
            pos = (pos - length) % 100
        else:
            pos = (pos + length) % 100
        
        if pos == 0:
            at_zero += 1
    
    return at_zero

print(sol())