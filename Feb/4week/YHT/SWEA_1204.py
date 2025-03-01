T = int(input())

for i in range(1, T + 1):
    _ = int(input())  # 입력 개수는 사용하지 않으므로 무시
    a = list(map(int, input().split()))
    
    count2 = [0] * 101  # 0~100까지 등장 횟수 저장
    c = 0  # 최빈값 저장 변수
    max2 = 0  # 최빈값의 등장 횟수

    for x in range(1000):  
        count2[a[x]] += 1  

    max2 = max(count2)  # 최빈값의 등장 횟수 찾기

    for num in a:  # 입력된 숫자 순회하면서 최빈값 중 가장 큰 값 찾기
        if count2[num] == max2 and num > c:
            c = num

    print(f'#{i} {c}')  # 최빈값 출력
