input_file = open('input.in', 'r')
Lines = input_file.read().strip()
# Lines = '^v^v^v^v^v'

santa_visited = set()
robo_santa_visited = set()
santa_visited.add((0, 0))
# robo_santa_visited.add((0, 0))
santa_pos = (0, 0)
robo_santa_pos = (0, 0)
n = 0
for i in Lines:
    if n == 0:
        if i == '^':
            santa_pos = (santa_pos[0], santa_pos[1] + 1)
        elif i == 'v':
            santa_pos = (santa_pos[0], santa_pos[1] - 1)
        elif i == '>':
            santa_pos = (santa_pos[0] + 1, santa_pos[1])
        elif i == '<':
            santa_pos = (santa_pos[0] - 1, santa_pos[1])
        santa_visited.add(santa_pos)
        n += 1
    else:
        if i == '^':
            robo_santa_pos = (robo_santa_pos[0], robo_santa_pos[1] + 1)
        elif i == 'v':
            robo_santa_pos = (robo_santa_pos[0], robo_santa_pos[1] - 1)
        elif i == '>':
            robo_santa_pos = (robo_santa_pos[0] + 1, robo_santa_pos[1])
        elif i == '<':
            robo_santa_pos = (robo_santa_pos[0] - 1, robo_santa_pos[1])
        robo_santa_visited.add(robo_santa_pos)
        n += -1

print(len(santa_visited) + len(robo_santa_visited))
