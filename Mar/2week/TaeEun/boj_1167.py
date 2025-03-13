import sys
sys.setrecursionlimit(10**6)

v = int(input())

child_lists = [[] for _ in range(v+1)]   # 부모를 인덱스로 자식을 담고있는 리스트
weights = [0]*(v+1)         # 자식을 인덱스로 부모와 연결된 가치를 저장
checked = [0]*(v+1)

for _ in range(v):
    edges = list(map(int, input().split()))
    start = edges.pop(0)
    checked[start] = 1
    edges.pop()

    for i in range(len(edges)//2):
        
        end_idx = 2*i
        end = edges[end_idx]
        if checked[end]:
            continue
        weight_idx = 2*i +1
        weight = edges[weight_idx]

        child_lists[start].append(end)
        weights[end] = weight

ans = 0

def postorder_traversal(node):
    child_list = child_lists[node]
    global ans
    if child_list != []:
        w_list = []
        for child in child_list:
            cur = postorder_traversal(child)
            w_list.append(cur)
        w_list.sort(reverse=True)
        ans = max(ans, sum(w_list[0:2]))
        return max(w_list) + weights[node]
    else:
        return weights[node]

root = 1 # 내맘대로 선언(트리는 모든 노드가 루트가 될 수 있음)
postorder_traversal(root)

print(ans)