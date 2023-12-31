import numpy as np
import sympy
import sys

filename = sys.argv[1]

if 'test' in filename:
    min_test_area = 7
    max_test_area = 27
else:
    min_test_area = 200000000000000
    max_test_area = 400000000000000
    


class Hailstone:
    def __init__(self, string):
        pos_str,v_str = string.split('@')
        self.id = string
        self.pos = [int(x.strip()) for x in pos_str.strip().split(',')]
        self.v = [int(x.strip()) for x in v_str.strip().split(',')]
    def __repr__(self):
        return f"Hailstone<pos={self.pos},v={self.v}>"
    def intersect_2d(self,other):
        temp_pos = (self.pos[0]-other.pos[0],self.pos[1]-other.pos[1])
        try:
            t1,t2 = sympy.symbols(['t1','t2'])
            system = [
                sympy.Eq(other.v[0]*t2-self.v[0]*t1,temp_pos[0]),
                sympy.Eq(other.v[1]*t2-self.v[1]*t1,temp_pos[1]),
            ]
            sol = sympy.solve(system, [t1,t2])
            if sol[t1] < 0 or sol[t2] < 0:
                return None
            ret = self.find_at_t(sol[t1])
            #ret2 = other.find_at_t(sol[t2])
            #assert ret == ret2, "rets dont equal"
            return ret
        except Exception as e:
            print(e)
            return None
    def find_at_t(self, t):
        scaled_v = [v*t for v in self.v]
        new_pos = [a+b for a,b in zip(self.pos,scaled_v)]
        return new_pos[:-1]


with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    stones = []
    for line in temp:
        stones.append(Hailstone(line))

    print(len(stones))
    ans = 0
    for i,h1 in enumerate(stones):
        for h2 in stones[:i]:
            #if not (h1.id == "19, 13, 30 @ -2,  1, -2" and h2.id == "18, 19, 22 @ -1, -1, -2"):
            #    continue
            temp = h1.intersect_2d(h2)
            if temp is not None and min_test_area <= temp[0] <= max_test_area and min_test_area <= temp[1] <= max_test_area:
                ans += 1


    print(ans) 
