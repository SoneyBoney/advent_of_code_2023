
filename = "input.txt"


def rotate(a):
    ret = [[None for _ in range(len(a))] for _ in range(len(a[0]))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            ret[j][len(ret[0])-i-1] = a[i][j]
    return ret


def sol(a):
    for j in range(len(a[0])):
        i = 0
        while i < len(a):
            if a[i][j] == '.':
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
    return a

def cycle(a):
    a = sol(a)
    a = rotate(a)
    a = sol(a)
    a = rotate(a)
    a = sol(a)
    a = rotate(a)
    a = sol(a)
    a = rotate(a)
    return a
    
        

def compute_load(a):
    ret = 0
    for i,row in enumerate(a):
        for elem in row:
            if elem == 'O':
                ret += len(a)-i 
    return ret

with open(filename) as f:
    temp = [list(x) for x in f.read().split('\n')[:-1]]

    if False:
        rets = []
        for k in range(1000): #000000):
            temp = cycle(temp)
            ret = compute_load(temp)
            rets.append(ret)
        print(rets)
    
    o = [100141, 100187, 100307, 100399, 100480, 100525, 100582, 100571, 100551, 100609, 100673, 100765, 100824, 100869, 100905, 100882, 100852, 100850, 100826, 100828, 100820, 100808, 100813, 100821, 100844, 100797, 100807, 100826, 100834, 100879, 100940, 101002, 101065, 101083, 101073, 101061, 101017, 100982, 100946, 100900, 100865, 100826, 100791, 100763, 100724, 100663, 100599, 100513, 100414, 100333, 100228, 100154, 100098, 100030, 99998, 99939, 99901, 99837, 99780, 99690, 99644, 99595, 99545, 99503, 99455, 99438, 99427, 99417, 99375, 99364, 99354, 99329, 99325, 99316, 99316, 99290, 99265, 99211, 99200, 99179, 99168, 99172]
    period = [99166, 99165, 99137, 99137, 99111, 99099, 99118, 99131, 99162, 99150, 99139, 99142, 99146, 99095, 99112, 99133, 99147, 99146, 99124, 99144, 99151, 99130, 99108, 99127, 99149, 99131, 99120, 99129, 99153, 99135, 99143, 99123, 99143, 99133, 99105, 99125, 99138, 99137, 99148, 99158, 99139, 99127, 99107, 99110, 99134, 99122, 99150, 99163, 99174, 99123, 99101, 99112, 99119, 99118, 99135, 99165, 99179, 99158, 99097, 99106, 99121, 99103, 99131, 99150, 99181, 99163, 99132, 99102, 99115, 99105, 99116, 99146]
    offset = (1000000000 - len(o)-1) % len(period)

    print(period[offset])
