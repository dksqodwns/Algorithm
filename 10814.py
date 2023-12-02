N = int(input())

members = []
for _ in range(N):
    age, name = input().split()
    age = int(age)
    members.append((age, name))

members.sort(key=lambda x: x[0])

for i in members:
    print(i[0], i[1])
