lines = open('input.txt', 'r').readlines()

count = 0


def pairRepeat(s):
    i = 0
    r = 0
    while i < len(s) - 1:
        subString = s[i] + s[i+1]
        if s.count(subString) >= 2:
            r = 1
            break
        else:
            r = 0
        i += 1
    return r


def letterRepeat(s):
    i = 0
    r = 0
    while i < len(s) - 2:
        if s[i] == s[i+2]:
            r = 1
            break
        else:
            r = 0
        i += 1
    return r


for s in lines:
    if pairRepeat(s) == 1 and letterRepeat(s) == 1:
        count += 1
print(count)
