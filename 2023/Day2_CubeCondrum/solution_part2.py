input_file = open('input.txt', 'r')
Lines = input_file.readlines()


def minimum_cubes(game_result):
    red = 0
    green = 0
    blue = 0
    game_result = game_result.split(':')
    game_result = game_result[1].split(';')
    for i in game_result:
        round = i.split(',')
        for r in round:
            r = r.strip()
            values = r.split(' ')
            if values[1] == 'red':
                if int(values[0]) > red:
                    red = int(values[0])
            if values[1] == 'green':
                if int(values[0]) > green:
                    green = int(values[0])
            if values[1] == 'blue':
                if int(values[0]) > blue:
                    blue = int(values[0])

    return red*blue*green


print(minimum_cubes('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'))
