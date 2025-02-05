# 📄 boj_2805_나무자르기
https://www.acmicpc.net/problem/2805

## 1. 시간초과 이슈
시간초과가 나서 여러 수정을 거쳤다. 
보통 미미한 부분이긴 하나 해당 문제에선 N이 커서(최대 1,000,000) 꽤 영향이 있는 듯하다.   
실제로 해당 부분만 변경했음에도 시간이 4932ms -> 2156ms로 줄어들었다.

###  [1] for문 VS 리스트 컴프리헨션
####  수정 전 코드 (시간초과)
```
count = 0
for tree in trees:
    if tree > mid:
        count += tree - mid   
```
####  수정 후 코드
```
count = sum(tree - mid for tree in trees if tree > mid)
```
for문과 리스트컴프리헨션은 이론상 O(N)으로 같은 시간복잡도를 갖지만
리스트컴프리헨션은 파이썬 내부적으로 최적화가 되어있어
N이 클 경우 훨씬 빠르다.
문제 조건에서 N은 최대 1,000,000 크기를 갖기 때문에
리스트컴프리헨션을 활용하면 조금 더 효율적일 것이다.

###  [2] 입출력
####  수정 전 코드 (시간초과)
```
import sys
N, M = map(int, sys.stdin.readline().strip().split())
trees = list(map(int, sys.stdin.readline().strip().split()))
```
####  수정 후 코드
```
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
```

## 2. 정렬을 해야할까
### 이진탐색을 활용하는데 정렬을 안하고도 정상적으로 동작한 이유
trees 배열 중에서 특정 값을 찾는 문제가 아니고 적절한 절단기 높이를 조정해야 하는 문제이기 때문.

정렬된 배열에서 특정 값 X가 존재하는지 찾는 경우였다면,
mid 값을 비교할 때 오름차순 정렬이 되어 있어야 했을 것.

# 📄 sea_2001_파리퇴치
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq

M*M 크기를 구하기 위해 bfs 탐색을 했는데 배보다 배꼽이 큰 느낌이 든다. 

- 그 외 방식
    - 누적 합
    - 완전 탐색(4중 for문)

## [1] M*M크기 탐색할 때 주의점
탐색시 항상 상하좌우로만 탐색하는게 아니다. 문제마다 다르게 방향 설정 필요..
이 문제는 우측 하측 방향으로만 탐색하면 됐었다.

```
# 4방향(상하좌우) 탐색..은 안된다.
# 상측, 좌측까지 탐색하면 M*M 크기보다 탐색 영역이 넓어지기 때문이다.
# 시작 위치를 기준으로 오른쪽&하단으로 점차 퍼지면서 탐색해야 한다.
# dr = [-1, 0, 1, 0] 
# dc = [0, 1, 0, -1]

# 2방향(우,하) 탐색
dr = [0, 1]
dc = [1, 0]
```
