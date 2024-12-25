input_file = open('demo_input.txt', 'r')
levels = input_file.readlines()
current_level = []

for i in levels:
    j = 1
    status = 0
    current_level = i
    current_level = current_level.split()
    while j < len(current_level):
        if (abs(int(current_level[j-1]) - int(current_level[j]))) <= 3:
            status = 1
        else:
            status = 0
        j += 1
    print(status)
