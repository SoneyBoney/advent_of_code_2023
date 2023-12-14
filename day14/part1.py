
filename = "input.txt"



def sol(a):
    for j in range(len(a[0])):
        i = 0
        while i < len(a):
            if a[i][j] == '.':
                print(i,j)
                #look for next valid O 
                for k in range(i,len(a)):
                    if a[k][j] == '#':
                        i = k+1
                        break
                    if a[k][j] == '.':
                        continue
                    a[k][j] = '.'
                    a[i][j] = 'O'
                    i += 1
                    break
                else:
                    i = len(a)
            else:
                i += 1
            for row in a:
                print("".join(row))
            print()
        print('================')
    return a


with open(filename) as f:
    temp = [list(x) for x in f.read().split('\n')[:-1]]


    a = sol(temp)
    ret = 0
    for i,row in enumerate(a):
        for elem in row:
            if elem == 'O':
                ret += len(a)-i 

    print(ret)
