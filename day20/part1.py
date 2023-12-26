import math
from collections import deque
from enum import Enum

filename = "input.txt" 

class Pulse(Enum):
    Low = 0
    High = 1

class State(Enum):
    Off = 0
    On = 1

class FlipFlop:
    def __init__(self, name: str):
        self.name = name
        self.state = State.Off 
        self.dests = []
        self.send_queue = deque()
    def __repr__(self):
        return f"FlipFlop<Name={self.name},Dests={[x.name for x in self.dests]}"
    def add_destination(self, dest):
        self.dests.append(dest) 
        dest.add_parent(self)
    def add_parent(self, parent):
        pass
    def receive(self, sender: str, pulse: Pulse):
        if pulse == Pulse.High:
            return
        if self.state == State.Off:
            self.state = State.On
            self.send_queue.append(Pulse.High) 
        else:
            self.state = State.Off
            self.send_queue.append(Pulse.Low)
    def send(self,Q,count):
        if not self.send_queue:
            return
        pulse = self.send_queue.popleft()
        for child in self.dests:
            child.receive(self.name, pulse)
            count[pulse] += 1
            Q.append(child)

class Conjunction:
    def __init__(self, name: str):
        self.name = name
        self.memory = {}
        self.dests = []
        self.send_queue = deque()
    def __repr__(self):
        return f"Conjunction<Name={self.name},Dests={[x.name for x in self.dests]}"
    def add_destination(self, dest):
        self.dests.append(dest) 
        dest.add_parent(self)
    def add_parent(self, parent):
        self.memory[parent.name] = Pulse.Low
    def receive(self, sender: str, pulse: Pulse):
        self.memory[sender] = pulse 
        if all([x==Pulse.High for x in self.memory.values()]):
            self.send_queue.append(Pulse.Low) 
        else:
            self.send_queue.append(Pulse.High)
    def send(self,Q, count):
        if not self.send_queue:
            return
        pulse = self.send_queue.popleft()
        for child in self.dests:
            child.receive(self.name, pulse)
            count[pulse] += 1
            Q.append(child)
        
class Broadcast:
    def __init__(self, name: str):
        self.name = name
        self.dests = []
        self.send_queue = deque()
    def __repr__(self):
        return f"Broadcast<Name={self.name},Dests={[x.name for x in self.dests]}"
    def add_destination(self, dest):
        self.dests.append(dest)
        dest.add_parent(self)
    def add_parent(self, parent):
        pass
    def receive(self, sender: str, pulse: Pulse):
        self.send_queue.append(pulse)
    def send(self, Q, count):
        if not self.send_queue:
            return
        pulse = self.send_queue.popleft()
        for child in self.dests:
            child.receive(self.name, pulse)
            count[pulse] += 1
            Q.append(child)
class DummyOut:
    def __init__(self, name: str):
        self.name = name
    def __repr__(self):
        return f"Dummy<Name={self.name}>"
    def add_destination(self, dest):
        pass
    def add_parent(self, parent):
        pass
    def receive(self, sender: str, pulse: Pulse):
        pass
    def send(self, Q, count):
        pass

def build_graph(module_list):
    ret = {}
    for m in module_list:
        name = m.split('->')[0].strip()
        key = name.removeprefix('%').removeprefix('&')
        if '%' in name:
            ret[key] = FlipFlop(key)
        elif '&' in name:
            ret[key] = Conjunction(key)
        else:
            ret[key] = Broadcast(key)
    print(ret)
    for m in module_list:
        name = m.split('->')[0].strip().removeprefix('%').removeprefix('&')
        children = [x.strip() for x in m.split('->')[1].strip().split(',') if x]
        this_module = ret[name]
        for child in children:
            if child in ret:
                module_ptr = ret[child]
            else:
                module_ptr = DummyOut(child)
            this_module.add_destination(module_ptr) 
    return ret


with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    G = build_graph(temp)

    print(G)
    count = {p:0 for p in Pulse}

    for _ in range(1000):
        G['broadcaster'].receive('init', Pulse.Low) 
        Q = deque([G['broadcaster']])
        count[Pulse.Low] += 1
        while Q:
            curr_module = Q.popleft()
            curr_module.send(Q,count)


    print(count)
    print(math.prod(count.values()))
