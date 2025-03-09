# 스도쿠 퍼즐을 검사하기 위한 함수 생성
def checklist(arr):
    return sorted(arr) == list(range(1, 10))

T = int(input())

for tc in range(1, T+1):
    # 스도쿠 퍼즐 입력 받기
    arr = [list(map(int, input().split())) for _ in range(9)]
    # 스도쿠 검사하는 플래그
    isClear = True

    # 가로 검사
    for i in range(9):
        if not checklist(arr[i]):
            isClear = False
            break
    
    # 세로 검사
    if isClear:
        for i in range(9):
            a_list = [arr[j][i] for j in range(9)]
            if not checklist(a_list):
                isClear = False
                break

    # 3×3 박스 검사
    if isClear:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box = []
                for x in range(3):
                    for y in range(3):
                        box.append(arr[i + x][j + y])
                if not checklist(box):
                    isClear = False
                    break
            if not isClear:
                break

    # 결과 출력
    ans = 1 if isClear else 0
    print(f'#{tc} {ans}')
