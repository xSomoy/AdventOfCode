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
        print(round[0].split(' '))
    return game_result


print(is_possible('Game 1: 3 blue, 2 green, 6 red; 17 green, 4 red, 8 blue; 2 red, 1 green, 10 blue; 1 blue, 5 green'))
