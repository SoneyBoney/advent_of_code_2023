import math
import copy

filename = "input.txt"


class Cond:
    def __init__(self, cond_str_full: str):
        if ':' in cond_str_full:
            cond_str,out_state = cond_str_full.split(':')
            self.terminal = False
        else:
            cond_str = cond_str_full
            out_state = cond_str_full
            self.terminal = True
        self.out_state = out_state
        if '<' in cond_str:
            var,val = cond_str.split('<')
            self.val = int(val)
            self.comp = '<'
        elif '>' in cond_str:
            var,val = cond_str.split('>') 
            self.val = int(val)
            self.comp = '>'
        else:
            var = None
            self.comp = None
            self.val = None
        self.name = var
    def process(self, item, Q, curr_state, history):
        if self.terminal:
            new_item = copy.deepcopy(item)
            new_history = copy.deepcopy(history)
            new_history.append(curr_state)
            Q.append((self.out_state,new_item, new_history))
            return None
        same_wf_int, next_wf_int = self.split_intervals(item)
        if next_wf_int is not None:
            next_item = copy.deepcopy(item)
            if self.name in next_item:
                del next_item[self.name]
            next_item[self.name] = next_wf_int
            new_history = copy.deepcopy(history)
            new_history.append(curr_state)
            Q.append((self.out_state,next_item,new_history))
        if same_wf_int is not None:
            if self.name in item:
                del item[self.name]
            item[self.name] = same_wf_int
            return item
        return None
    def split_intervals(self, item):
        midpoint = self.val
        interval = item[self.name]
        if midpoint < interval[0]:
            left = None
        else:
            left = (interval[0], midpoint)
        if midpoint >= interval[1]:
            right = None
        else:
            right = (midpoint, interval[1])
        if self.comp == '<':
            return (right[0],right[1]),left
        elif self.comp == '>':
            return (left[0],left[1]+1),(right[0]+1,right[1])
    def __repr__(self):
        return f"Cond: {self.name} {self.comp} {self.val}"

def str_to_dict(p):
    ret = {}
    str_p = p[1:-1]
    for pair_str in str_p.split(','):
        k,v_str = pair_str.split('=')
        v = int(v_str)
        ret[k] = v 
    return ret

with open(filename) as f:
    workflows_str,_ = f.read().split('\n\n')
    workflows = workflows_str.split('\n')
    workflow_dict = {}
    for wf in workflows:
        name,cond_str = wf.split('{')
        cond_str = cond_str[:-1]
        conds = cond_str.split(',')
        
        workflow_dict[name] = [Cond(x) for x in conds]
    Q = [('in', {'x':(1,4001), 'm':(1,4001), 'a':(1,4001), 's':(1,4001)},[])]
    ans = 0
    num_A = 0
    while Q:
        state,item,history = Q.pop(0)
        print(state,item,history)
        #if item is None:
        #    continue
        if state == 'R':
            continue
        elif state == 'A':
            num_A += 1
            ans += math.prod([x[1]-x[0] for x in item.values()])
            continue 
        wf = workflow_dict[state]
        for cond in wf:
            item = cond.process(item, Q, state, history)
            if item is None:
                break
    print(ans)        
    
    print('As: ', num_A)

