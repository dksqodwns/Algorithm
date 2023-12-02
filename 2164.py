# 맨 앞의 값을 삭제
# 맨 앞의 값을 맨 뒤로 이동 == 맨 뒤로 맨 앞의 값을 삽입

# 배열의 삽입, 삭제는 O(N)의 시간복잡도를 갖고있음. => 삽입이나 삭제를 할때 값을 다 밀거나, 땡기거나 하기 때문에

# 2초 안에 풀어야하는데, N이 최대 500,000이라서 (N-1)X만큼 1, 2번을 수행해야 함. 여기서는 세번을 하고있기때문에 (N-1)X(3XO(N)) = O(3N(N-1)) => 가장 큰 항이 N^2라서 시간복잡도가 O(N^2) 1초에 보통 10^8정도 계산 가능

# => 풀수없음

# ==> 원형 큐를 사용 pop 한번, push 한번

from collections import deque
import time

N = int(input("N을 입력하세요: "))

start_time = time.time()  # 시작 시간 기록

dq = deque(range(1, N+1))
while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq.pop())

# arr = [*range(1, N+1)]
# while len(arr) > 1:
#     arr.pop(0)
#     arr.append(arr.pop(0))
# print(arr.pop())

end_time = time.time()  # 종료 시간 기록
elapsed_time = end_time - start_time  # 경과 시간 계산

print(f"실행 시간: {elapsed_time} 초")
