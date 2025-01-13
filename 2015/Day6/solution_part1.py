lines = open('input.txt', 'r').readlines()
# lights[999, 999] = {0}


def turnOn(start, end):
    print("On:")
    x1 = int(start.split(",")[0])
    y1 = int(start.split(",")[1])
    x2 = int(end.split(",")[0])
    y2 = int(end.split(",")[1])
    print("x1 = ", x1)
    print("y1 = ", y1)
    print("x2 = ", x2)
    print("y2 = ", y2)


def toggle(start, end):
    print("Toggle:")
    x1 = int(start.split(",")[0])
    y1 = int(start.split(",")[1])
    x2 = int(end.split(",")[0])
    y2 = int(end.split(",")[1])
    print("x1 = ", x1)
    print("y1 = ", y1)
    print("x2 = ", x2)
    print("y2 = ", y2)


def turnOff(start, end):
    print("Off:")
    x1 = int(start.split(",")[0])
    y1 = int(start.split(",")[1])
    x2 = int(end.split(",")[0])
    y2 = int(end.split(",")[1])
    print("x1 = ", x1)
    print("y1 = ", y1)
    print("x2 = ", x2)
    print("y2 = ", y2)


for i in lines:
    if i.split()[0] == "toggle":
        toggle(i.split()[1], i.split()[3])
    elif i.split()[1] == "on":
        turnOn(i.split()[2], i.split()[4])
    elif i.split()[1] == "off":
        turnOff(i.split()[2], i.split()[4])
