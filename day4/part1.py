




def sol(a):
    card_ind, nums = a.split(':')
    winning, hand = nums.strip().split('|')

    winning_set = set([int(x.strip()) for x in winning.split(' ') if x])
    hand_set = set([int(x.strip()) for x in hand.split(' ') if x])

    common = winning_set.intersection(hand_set)
    return 1 << (len(common) - 1) if len(common) else 0



with open('input.txt') as f:
    a = f.read().split('\n')[:-1]

    ans = [sol(x) for x in a]

    print(sum(ans))
