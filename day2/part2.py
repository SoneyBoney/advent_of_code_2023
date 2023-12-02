import math
def sol(input_str):
    game_id_str,turns = input_str.split(':')
    game_id = int(game_id_str.removeprefix('Game '))
    turn_list = [x.strip() for x in turns.strip().split(';')]
    min_dict = {"red": 0, "green": 0, "blue": 0}
    for turn in turn_list:
        temp = [x.strip() for x in turn.split(',')]
        for color_num in temp:
            num,color = color_num.split(' ')
            if int(num) > min_dict[color]:
                min_dict[color] = int(num)
    return math.prod(min_dict.values())
with open('example.txt') as f:
    temp = f.read().split('\n')[:-1]
    ret = 0
    for game in temp:
        ret += sol(game)

    print(ret)
