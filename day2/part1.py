

limits = {"red": 12, "green": 13, "blue": 14}


def sol(input_str):
    game_id_str,turns = input_str.split(':')
    game_id = int(game_id_str.removeprefix('Game '))
    turn_list = [x.strip() for x in turns.strip().split(';')]

    for turn in turn_list:
        temp = [x.strip() for x in turn.split(',')]
        for color_num in temp:
            num,color = color_num.split(' ')
            if int(num) > limits[color]:
                return 0
    return game_id


with open('input.txt') as f:
    temp = f.read().split('\n')[:-1]
    ret = 0
    for game in temp:
        ret += sol(game)

    print(ret)
