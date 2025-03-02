# 📄 2206_벽 부수고 이동하기
https://www.acmicpc.net/problem/2206
## 1. 잔잔바리 실수들
### [1] N, M 좌표 오류
문제에서 좌표 범위가 (1, 1) ~ (N, M)이다. 0이 아닌 1부터 시작한다는 것을 고려해야 한다.
- 목표 지점은 N-1, M-1이 되어야 한다.
- 범위 밖을 체크할 때, **nr >= N, nc >= M** 인지 확인해야 한다.   
    나는 목표 지점이 N-1, M-1이라 범위 밖도 nr >= N-1, nc >= M-1로 설정해야 된다고 잘못 생각했었다. 하지만 실제 좌표는 (0, 0) ~ (N-1, M-1)이므로 (N-1, M-1)도 이동할 수 있는 좌표가 맞다.

### [2] 거리 업데이트 실수
#### 수정 전 코드
```
visited[nr][nc][1] = graph[row][col] + 1 # 거리 업데이트
```

#### 수정 후 코드
이동 거리는 visited 배열에 저장하고 있었다.
```
visited[nr][nc][1] = visited[row][col][crushed] + 1 # 거리 업데이트
```

### [3] 얕은 복사 오류
```
visited = [[[-1, -1]] * M for _ in range(N)] # 얕은 복사 오류

visited = [[[-1, -1] for _ in range(M)] for _ in range(N)] # 깊은 복사 
```

### [4] visited 시작 위치 초기화 오류
시작점에서 출발할 때 벽 안 부순 차원만 거리를 업데이트 해서, 부순 차원에선 시작점을 다시 방문하게 되는 문제가 있었다.

#### 수정 후 코드
```
queue.append((0, 0, 0)) # row, col, 벽 부쉈는지
visited[0][0][0] = 1 # 벽 안 부순 차원 거리 업데이트
visited[0][0][1] = 1 # 벽 부순 차원 거리 업데이트
```


# 📄 5215_햄버거 다이어트
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT

## 1. 설계시 이슈
### [1] 그리디 or 완탐
(맛 / 칼로리) 비율을 계산하여, 해당 비율이 높은 순대로 더하려고 하였다.  
하지만 이런 그리디한 접근방식이 맞진 않았다.  
해당 비율로 계산했을 때 꼭 최적해를 구할 수 있다고 보장할 순 없기 때문이다.  
#### 수정 전 코드 (그리디)
```
    for i in range(N):
        T, K = map(int, input().split())
        food.append((T / K, T, K))

    total = 0
    food.sort(reverse=True)
    for percent, t, k in food:
        if total + k > L:
            continue 
        total += t
        
    print(f"#{test_case} {total}")
```

예를 들어 아래와 같이 세가지 음식이 있을 때를 가정해보자.
```
1) 맛 80, 칼로리 40 -> (비율 2)
2) 맛 100, 칼로리 60 -> (비율 5/3)
3) 맛 50, 칼로리 30 -> (비율 5/3) 
```

**제한 칼로리가 90일 때**
- 비율 순대로 조합을 뽑는 경우:  
1번 선택되고 끝난다.   
80점.

- 실제 정답:  
2,3번 조합이 점수가 더 높다.   
150점.


>따라서 **완전탐색**으로 모든 경우의 수를 따져봐야 한다.  
이 때 itertools의 combination을 사용하여 모든 케이스마다 실행할 수 있겠지만  
백트래킹을 하기 위해 **dfs**로 구현하였다.