x = 123

xbin = bin(x)[2:].zfill(16)
notxbin = "".join('1' if c == '0' else '0' for c in xbin)
intnotxbin = int('0b' + notxbin, 2)
print(xbin)
print(notxbin)
print(intnotxbin)
