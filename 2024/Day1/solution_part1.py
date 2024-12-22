input_file = open('input.txt', 'r')
Lines = input_file.readlines()
left_col = []
right_col = []


for i in Lines:
    left_col.append(i.split()[0])
left_col = sorted(left_col)


for i in Lines:
    right_col.append(i.split()[1])
right_col = sorted(right_col)

distance = 0
i = 0
while (i < len(left_col)):
    distance = distance + abs((int(right_col[i]) - int(left_col[i])))
    i += 1
print(distance)
