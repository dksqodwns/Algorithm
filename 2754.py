s = input()

if s.startswith('A'):
    if s.endswith('+'):
        print(4.3)
    elif s.endswith('0'):
        print(4.0)
    elif s.endswith('-'):
        print(3.7)
elif s.startswith('B'):
    if s.endswith('+'):
        print(3.3)
    elif s.endswith('0'):
        print(3.0)
    elif s.endswith('-'):
        print(2.7)
elif s.startswith('C'):
    if s.endswith('+'):
        print(2.3)
    elif s.endswith('0'):
        print(2.0)
    elif s.endswith('-'):
        print(1.7)
elif s.startswith('D'):
    if s.endswith('+'):
        print(1.3)
    elif s.endswith('0'):
        print(1.0)
    elif s.endswith('-'):
        print(0.7)
else:
    print(0.0)
