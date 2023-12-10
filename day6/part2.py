import math

filename = "input.txt"



def sol(b,c):
    root1 = (b + math.sqrt(b**2 - 4*c))/2
    root2 = (b - math.sqrt(b**2 - 4*c))/2

    ret1 = min(root1,root2)
    ret2 = max(root1,root2)

    ret1 = math.ceil(ret1)
    ret2 = math.floor(ret2) 

    return (ret2-ret1) + 1


with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    time = int("".join(temp[0].removeprefix('Time:').strip().split()))

    distance = int("".join(temp[1].removeprefix('Distance:').strip().split()))


    ans = sol(time,distance)

    print(ans)

