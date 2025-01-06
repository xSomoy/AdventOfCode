input_file = open('input.txt', 'r')
Lines = input_file.read().strip()

visited = set()
visited.add((0, 0))
pos = (0, 0)

for i in Lines:
    if i == '^':
        pos = (pos[0], pos[1] + 1)
    elif i == 'v':
        pos = (pos[0], pos[1] - 1)
    elif i == '>':
        pos = (pos[0] + 1, pos[1])
    if i == '<':
        pos = (pos[0] - 1, pos[1])
    visited.add(pos)
print(len(visited))
