lines = open('input.txt', 'r').readlines()

count = 0


def bannedStrings(s):
    if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
        return 0
    else:
        return 1


def vowelCount(s):
    vCount = 0
    for c in s:
        if c in 'aeiou':
            vCount += 1
    if vCount > 2:
        return 1
    else:
        return 0


def charRepeat(s):
    i = 0
    r = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            r = 1
            break
        else:
            r = 0
        i += 1
    return r


for s in lines:
    if bannedStrings(s) == 1 and vowelCount(s) == 1 and charRepeat(s) == 1:
        count += 1

print(count)
