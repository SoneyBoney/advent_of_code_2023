import numpy as np
import sympy
import sys

filename = sys.argv[1]


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

    t,x1,x2,x3,v1,v2,v3 = sympy.symbols(['t','x1','x2','x3','v1','v2','v3'])
    system = []
    variables = [x1,x2,x3,v1,v2,v3]
    for i,line in enumerate(temp):
        pos_str,v_str = line.split('@')
        pos = [int(x.strip()) for x in pos_str.strip().split(',')]
        v = [int(x.strip()) for x in v_str.strip().split(',')]
        
        t = sympy.symbols([f't{i}'])[0]
        variables.append(t)
        print(t)
        system += [
            sympy.Eq(pos[0]+v[0]*t,x1+v1*t),
            sympy.Eq(pos[1]+v[1]*t,x2+v2*t),
            sympy.Eq(pos[2]+v[2]*t,x3+v3*t),
        ]
        if i > 4:
            break
    
    print(system)
    print(variables)

    sol = sympy.solve(system, variables)
    print(sol)
    sol = sol[0]
    print(sol[0]+sol[1]+sol[2])
        
    


