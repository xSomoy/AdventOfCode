import hashlib


def md5(key):
    return hashlib.md5(key.encode()).hexdigest()


# seed = "abcdef609043"
seed = "yzbqklnj"
num = 0
while True:
    key = seed + str(num)
    result = md5(key)
    if result[0] == '0' and result[1] == '0' and result[2] == '0' and result[3] == '0' and result[4] == '0':
        print("Hash starts with 5 zeros")
        print(key + " md5 hash:  " + result)
        print(num)
        exit()
    num += 1
