import sys

number = int(sys.stdin.readline())
s = []
num_time = 1
result = 0
for i in range(number):
    s.append(number - i)

for i in s:
    num_time *= i

list_number = list(str(num_time))[::-1]

for i in list_number:
    if i == '0':
        result += 1
    else:
        break

print(result)
