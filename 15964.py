x, y = map(int, input().split())


def commercial(a, b):
    result = (a + b) * (a - b)
    print(result)


commercial(x, y)
