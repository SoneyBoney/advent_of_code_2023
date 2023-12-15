
filename = "input.txt"



def sol(s):
    current = 0
    for c in s:
        ascii_val = ord(c)
        current += ascii_val
        current *= 17
        current %= 256
    return current


with open(filename) as f:
    temp = f.read().split('\n')[:-1][0].split(',')

    print(temp)


    ret = 0
    for s in temp:
        ret += sol(s)


    print(ret)
