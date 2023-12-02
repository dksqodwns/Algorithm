while True:
    S = input()
    count = 0
    if len(S) <= 100 and len(S) <= 0 and not S.startswith('') and not S.endswith(''):
        print(S)
        count += 1
    elif S.startswith('') or S.endswith('') or count > 100:
        break
