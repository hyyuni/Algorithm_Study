import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("input.txt", "r") # 표준 입력을 파일로 변경
# input = sys.stdin.readline

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]
rev = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    A = []
    for _ in range(K):
        A.append(list(map(int, input().split())))

    for _ in range(M):
        info = dict()
        for row in range(K):
            r, c, k, d = A[row]
            if not k:
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            
            A[row][0], A[row][1] = nr, nc
            if not (1 <= nr < N-1 and 1 <= nc < N-1):
                A[row][2] //= 2  # 수
                A[row][3] = rev[d]  # 방향
            if (nr, nc) not in info.keys():
                info[(nr, nc)] = [row, k]

            else:
                num, size = info[(nr, nc)]
                next_size = A[row][2]
                if  next_size > size:
                    info[(nr, nc)] = [row, next_size]  # 바꿔주기
                    A[row][2] += A[num][2]  # 더하기
                    A[num][2] = 0  # 기존 거 사이즈 삭제
                else:
                    A[num][2] += A[row][2]
                    A[row][2] = 0
    microbe = 0
    for m in A:
        microbe += m[2]  # 남아있는 군집 사이즈 더하기
    
    print(f"#{tc+1} {microbe}")
