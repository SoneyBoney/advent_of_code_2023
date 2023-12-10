from collections import defaultdict

filename = "input.txt"

card_val_map = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "T": 10,
    "J": 1
}

def get_kind_num(cards):
    ccs = sorted(cards.values())
    if ccs == [5]: return 7
    if ccs == [1,4]: return 6
    if ccs == [2,3]: return 5
    if ccs == [1,1,3]: return 4
    if ccs == [1,2,2]: return 3
    if ccs == [1,1,1,2]: return 2
    if ccs == [1,1,1,1,1]: return 1
    raise RuntimeError(f"should not happen: {cards}")
    

        
class Card:
    def __init__(self,card_str: str):
        self.card_str = card_str
        self.card_dict = defaultdict(int)
        for c in self.card_str:
            self.card_dict[c] += 1
        if 'J' in self.card_dict.keys():
            #coerce to best kind
            num_js = self.card_dict['J']
            del self.card_dict['J']
            if not self.card_dict.items():
                self.card_dict['J'] = 0
            max_item = max(self.card_dict.items(),key=lambda x: x[1])
            self.card_dict[max_item[0]] += num_js
    def __lt__(self,other):
        kind_num_a = get_kind_num(self.card_dict)
        kind_num_b = get_kind_num(other.card_dict)
        print(self, other)
        if kind_num_a != kind_num_b:
            return kind_num_a < kind_num_b
        for char_a,char_b in zip(self.card_str,other.card_str):
            val_a = int(char_a) if char_a.isdigit() else card_val_map[char_a]
            val_b = int(char_b) if char_b.isdigit() else card_val_map[char_b]
            if val_a < val_b:
                return True
            elif val_a > val_b:
                return False
        raise RuntimeError("shuold never happen")
        return False
        
    
    def __repr__(self):
        return f"Card<{self.card_str}>"



with open(filename) as f:
    temp = f.read().split('\n')[:-1]

    card_list = []
    card_dict = {}
    for t in temp:
        cards,val = t.split()
        card_list.append(Card(cards))
        card_dict[cards] = int(val)

    print(card_list)
    print(sorted(card_list))

    card_list.sort()

    ans = 0
    for i,card in enumerate(card_list):
        ans += (i+1)*card_dict[card.card_str] 
        print(card)
        print(f"adding: {i+1} * {card_dict[card.card_str]}")

    print(ans)
    
        
