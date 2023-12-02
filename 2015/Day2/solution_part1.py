input_file = open('input.txt', 'r')
Lines = input_file.readlines()


def cal_wrapper(dimention):
    total = 0
    a, b, c = map(int, dimention.split('x'))
    surface = 2*(a*b + a*c + b*c)
    slack = min(a*b, a*c, b*c)
    total = surface + slack
    return total


sum = 0
for line in Lines:
    sum += cal_wrapper(line)
# print(cal_wrapper(line))

print(sum)


# 1585300
