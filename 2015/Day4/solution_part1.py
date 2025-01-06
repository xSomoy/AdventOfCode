import hashlib


def md5(key):
    return hashlib.md5(key.encode()).hexdigest()


key = "yzbqklnj"
print(md5(key))
