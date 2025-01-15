import numpy as np
lines = open('input.txt', 'r').readlines()
# lines = open("demo.in", 'r').readlines()

lights = np.zeros((1000, 1000))


def turnOn(start, end):
    x1 = int(start.split(",")[0])
    y1 = int(start.split(",")[1])
    x2 = int(end.split(",")[0])
    y2 = int(end.split(",")[1])
    while x1 <= x2:
        while y1 <= y2:
            lights[x1][y1] = 1
            y1 += 1
        y1 = int(start.split(",")[1])
        x1 += 1


def toggle(start, end):
    x1 = int(start.split(",")[0])
    y1 = int(start.split(",")[1])
    x2 = int(end.split(",")[0])
    y2 = int(end.split(",")[1])
    while x1 <= x2:
        while y1 <= y2:
            if lights[x1][y1] == 1:
                lights[x1][y1] = 0
            elif lights[x1][y1] == 0:
                lights[x1][y1] = 1
            y1 += 1
        y1 = int(start.split(",")[1])
        x1 += 1


def turnOff(start, end):
    x1 = int(start.split(",")[0])
    y1 = int(start.split(",")[1])
    x2 = int(end.split(",")[0])
    y2 = int(end.split(",")[1])
    while x1 <= x2:
        while y1 <= y2:
            lights[x1][y1] = 0
            y1 += 1
        y1 = int(start.split(",")[1])
        x1 += 1


for i in lines:
    if i.split()[0] == "toggle":
        toggle(i.split()[1], i.split()[3])
    elif i.split()[1] == "on":
        turnOn(i.split()[2], i.split()[4])
    elif i.split()[1] == "off":
        turnOff(i.split()[2], i.split()[4])

sum = 0
for row in lights:
    for element in row:
        sum += element


print(lights)
print(sum)
