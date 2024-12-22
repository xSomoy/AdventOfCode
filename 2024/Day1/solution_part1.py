input_file = open('demo_input.txt', 'r')
Lines = input_file.readlines()
left_col = []
right_col = []


for i in Lines:
    left_col.append(i.split()[0])
left_col = sorted(left_col)


for i in Lines:
    right_col.append(i.split()[1])
right_col = sorted(right_col)

i = 0
while (0 < len(left_col)):
    print(int(left_col[i]) - int(right_col[i]))
    i += 1
