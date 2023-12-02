N, X = map(int, input().split())
number_list = list(map(int, input().split()))

result = [str(num) for num in number_list if X > num]
print(' '.join(result))
