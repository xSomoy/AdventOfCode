input_file = open('input.txt', 'r')
Lines = input_file.readlines()


def is_possible(game_result):
    red = 12
    green = 13
    blue = 14
    game_result = game_result.split(':')
    game_result = game_result[1].split(';')
    for i in game_result:
        round = i.split(',')
        for r in round:
            r = r.strip()
            values = r.split(' ')
            if values[1] == 'red':
                if int(values[0]) <= red:
                    continue
                else:
                    return 0
            if values[1] == 'green':
                if int(values[0]) <= green:
                    continue
                else:
                    return 0
            if values[1] == 'blue':
                if int(values[0]) <= blue:
                    continue
                else:
                    return 0
    return 1


def get_id(game_result):
    id = game_result.split(':')
    id = id[0].split(' ')
    id = int(id[1])
    return id


sum = 0
for line in Lines:
    possiblity = is_possible(line)
    if possiblity != 0:
        id = get_id(line)
        sum += id
print(sum)
