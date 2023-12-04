def sol(a, table, mem):
    card_ind, nums = a.split(':')
    winning, hand = nums.strip().split('|')
    card_num = int(card_ind.split(' ')[-1].strip())
    # TODO: check memoize table
    if card_num in mem.keys():
        return mem[card_num]
    winning_set = set([int(x.strip()) for x in winning.split(' ') if x])
    hand_set = set([int(x.strip()) for x in hand.split(' ') if x])
    common = winning_set.intersection(hand_set)
    total = 1
    for i in range(card_num,card_num+len(common)):
        total += sol(table[i], table, mem)
    mem[card_num] = total
    return total



with open('input.txt') as f:
    a = f.read().split('\n')[:-1]

    mem = {}
    total = 0 
    for card in a:
        total += sol(card, a, mem)
        

    print(total)
