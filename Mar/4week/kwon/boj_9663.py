# 완전 이진 트리
# 중위 순회

k = int(input())
num = list(map(int, input().split()))
answer = [[] for _ in range(k)]

def dfs(num, depth):
    mid = (len(num) // 2) # 트리의 root index

    answer[depth].append(num[mid]) # 해당 깊이에 해당하는 node 추가

    if len(num) == 1:
        return

    dfs(num[:mid], depth+1)
    dfs(num[mid+1:], depth+1)

dfs(num, 0)

for i in answer:
    print(*i)
