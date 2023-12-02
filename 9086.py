T = int(input())

for _ in range(T):
    word = input()
    arr = list(word)
    first = arr[0]
    last = arr[len(word) - 1]

    print(first + last)
