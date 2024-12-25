input_file = open('demo_input.txt', 'r')
levels = input_file.readlines()
current_level = []
status = 1
for i in levels:
    j = 1
    current_level = i
    current_level = current_level.split()
    while j < len(current_level):
        if (int(current_level[j-1]) < int(current_level[j])):
            status += 1
        else:
            status -= 1
        j += 1

    if status < 4:
        print("Not Increasing")
    else:
        print("Increasing")
