input_file = open('input.txt', 'r')
Lines = input_file.readlines()


def cal_ribbon(dimention):
    total = 0
    a, b, c = map(int, dimention.split('x'))
    wrap = 2 * min(a+b, b+c, c+a)
    bow = a*b*c
    total = wrap + bow
    return total


sum = 0
for line in Lines:
    sum += cal_ribbon(line)

print(sum)

# print(cal_ribbon('1x1x10'))
