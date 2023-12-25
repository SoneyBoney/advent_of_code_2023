
filename = "input.txt"


class Cond:
    def __init__(self, cond_str_full: str):
        if ':' in cond_str_full:
            cond_str,out_state = cond_str_full.split(':')
        else:
            cond_str = cond_str_full
            out_state = cond_str_full
        self.out_state = out_state
        if '<' in cond_str:
            var,val = cond_str.split('<')
            self.func = lambda x: x < int(val)
        elif '>' in cond_str:
            var,val = cond_str.split('>') 
            self.func = lambda x: x > int(val)
        else:
            var = None
            self.func = lambda x: True
        self.name = var
    
    def next(self, item: dict):
        comp_val = item.get(self.name)
        if self.func(comp_val):
            return self.out_state
        return None 
        

def str_to_dict(p):
    ret = {}
    str_p = p[1:-1]
    for pair_str in str_p.split(','):
        k,v_str = pair_str.split('=')
        v = int(v_str)
        ret[k] = v 
    return ret


with open(filename) as f:
    workflows_str,parts_str = f.read().split('\n\n')


    workflows = workflows_str.split('\n')
    workflow_dict = {}

    for wf in workflows:
        name,cond_str = wf.split('{')
        cond_str = cond_str[:-1]
        conds = cond_str.split(',')
        
        workflow_dict[name] = [Cond(x) for x in conds]

    parts = parts_str.split('\n')[:-1]


    ans = 0
    for p in parts:
        item = str_to_dict(p)

        state = 'in'

        while state not in ['A','R']:
            wf = workflow_dict[state]

            for cond in wf:
                new_state = cond.next(item)
                if new_state is not None:
                    break

            state = new_state
        if state == 'A':
            ans += sum(item.values())

    print(ans)
    

