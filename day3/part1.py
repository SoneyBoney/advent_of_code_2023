import itertools as it

def sol(a):
    row = 0
    ret = []
    while row < len(a):
        col = 0
        while col < len(a[row]):
            stop_ind = col
            if a[row][col].isdigit():
                while stop_ind+1 < len(a[row]) and a[row][stop_ind+1].isdigit():
                    stop_ind += 1
                add_this = False
                for k in range(col, stop_ind+1):
                    for offset in it.product((0,1,-1),(0,1,-1)):
                        try:
                            if a[row+offset[0]][k+offset[1]] != '.' and (not a[row+offset[0]][k+offset[1]].isdigit()): 
                                add_this = True
                                break
                        except IndexError:
                            continue
                    if add_this:
                        break
                if add_this:
                    ret.append(int(a[row][col:stop_ind+1]))
            col = stop_ind + 1
        row += 1
    return ret





with open('input.txt') as f:
    temp = f.read().split('\n')[:-1]

    ret = sol(temp)
    print(sum(ret))
