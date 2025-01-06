instruction = open('input.txt', 'r').read().strip()

visited = set()
visited.add((0, 0))
pos = (0, 0)

n = 0
for i in instruction:
    if n == 0:
        if i == '^':
            pos = (pos[0], pos[1] + 1)
        elif i == 'v':
            pos = (pos[0], pos[1] - 1)
        elif i == '>':
            pos = (pos[0] + 1, pos[1])
        elif i == '<':
            pos = (pos[0] - 1, pos[1])
        visited.add(pos)
        n += 1
    elif n != 0:
        if i == '^':
            pos = (pos[0], pos[1] + 1)
        elif i == 'v':
            pos = (pos[0], pos[1] - 1)
        elif i == '>':
            pos = (pos[0] + 1, pos[1])
        elif i == '<':
            pos = (pos[0] - 1, pos[1])
        visited.add(pos)
        n -= 1


# print(visited)
print(len(visited))
