input_file = open('input.txt', 'r')
Lines = input_file.readlines()
left_col = []
right_col = []


for i in Lines:
    left_col.append(i.split()[0])


for i in Lines:
    right_col.append(i.split()[1])

similarity = 0

for i in left_col:
    count = 0
    for j in right_col:
        if j == i:
            count += 1
    similarity += int(i)*count

print(similarity)
