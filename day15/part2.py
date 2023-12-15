
filename = "input.txt"



def h(s):
    current = 0
    for c in s:
        ascii_val = ord(c)
        current += ascii_val
        current *= 17
        current %= 256
    return current


def remove(hm, key):
    index = h(key)
    item = None
    for i,pair in enumerate(hm[index]):
        if pair[0] == key:
            item = pair
    if not item:
        return
    hm[index].remove(item) 
    return
    

def add(hm, key, val):
    index = h(key)
    sub_index = -1
    for i,pair in enumerate(hm[index]):
        if pair[0] == key:
            sub_index = i
    if sub_index == -1:
        hm[index].append((key,val))
        return
    temp = (hm[index][sub_index][0], val)
    hm[index][sub_index] = temp
    return
    

def sol(hm, s):
    if '-' in s:
        key = s.removesuffix('-')
        remove(hm,key)
    else:
        key,val_str = s.split('=')
        val = int(val_str)
        add(hm, key, val)


with open(filename) as f:
    temp = f.read().split('\n')[:-1][0].split(',')

    hm = [[] for _ in range(256)]
    for s in temp:
        sol(hm,s)


    ret = 0
    for i,box in enumerate(hm):
        for j,slot in enumerate(box):
            ret += (1+i) * (1+j) * slot[1]    

    print(ret)


