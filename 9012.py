# VPS란? 괄호으 쌍이 완벽하게 맞춰져있는 것

for _ in range(int(input())):  # 몇개의 테스트 케이스를 작성 할 것 인지 결정
    stk = []  # 빈 배열 초기화
    isVPS = True  # VPS여부 초기화
    for ch in input():
        if ch == '(':  # 여는 괄호가 들어 올 때
            stk.append(ch)  # 리스트에 삽입
        else:  # 닫는 괄호가 들어 올 때
            if stk:  # 리스트가 비어있지 않으면 (여는 괄호가 있는 경우)
                stk.pop()  # 괄호 완성 => 여는 괄호 제거
            else:  # 리스트가 비어있으면 (여는 괄호가 없는 경우)
                isVPS = False  # VPS가 아님
                break  # 탈출
    if stk:  # 스택이 아직 남아있으면
        isVPS = False  # VPS가 아님

    print('YES' if isVPS else 'NO')  # VPS면 YES, VPS가 아니면 즉, 괄호가 쌍을 이루지 않으면 NO
