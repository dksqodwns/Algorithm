import time

# 시작 시간
start_time = time.time()

# 30분(1800초) 동안 실행
while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    # 현재 경과 시간을 분과 초로 변환
    minutes, seconds = divmod(int(elapsed_time), 60)

    # 콘솔에 경과 시간 출력
    print(f"Time elapsed: {minutes} minutes and {seconds} seconds")

    # 1분(60초)마다 메시지 출력
    if elapsed_time % 60 == 0:
        print("1 minute has passed")

    # 30분이 지나면 반복 종료
    if elapsed_time >= 1800:
        break

    # 1초 대기
    time.sleep(1)
