
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

def sol2():
    res = 0
    pos = 50

    f = open("./day01/input.txt")
    for line in f.readlines():
        direction = line[0]
        length = int(line[1:])
        passed_zero = False
        print(f"{direction} {length}")

        if direction == "L":
            while length >= 100:
                print("full rotation L")
                res += 1
                length -= 100
            
            prev_pos = pos
            pos = (pos - length) % 100
            if pos > prev_pos and prev_pos != 0:
                # we wrapped around!
                print(">>>passed zero going left")
                passed_zero = True
                res += 1
        else:
            while length >= 100:
                print("full rotation R")
                res += 1
                length -= 100
            
            prev_pos = pos
            pos = (pos + length) % 100
            if pos < prev_pos and prev_pos != 0:
                # we wrapped around!
                passed_zero = True
                print(">>>passed zero going right")
                res += 1
        
        if pos == 0 and not passed_zero:
            print(">>>currently on zero")
            res += 1
        
        print(f"pos={pos} res={res}")
        print("-----")

    return res

print(sol2())