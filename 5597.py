arr = [*range(1, 31)]

students = []

for i in range(28):
    t = int(input())
    students.append(t)

missing = sorted(list(set(arr) - set(students)))

for m in missing:
    print(m)
