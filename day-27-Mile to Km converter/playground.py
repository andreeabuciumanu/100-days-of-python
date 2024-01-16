def add(*args):
    s: int = 0
    for item in args:
        s += item
    return s


print(add(2, 4, 7, 9))