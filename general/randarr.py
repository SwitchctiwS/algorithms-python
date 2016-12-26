import random


def generate(n):
    random.seed(9001)

    arr = []
    if n is not None:
        for i in range(n):
            arr.append(i)

    else:
        for i in range(100):
            arr.append(i)

    random.shuffle(arr)
    return arr
