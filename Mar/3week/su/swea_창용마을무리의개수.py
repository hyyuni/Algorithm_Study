import sys
import os
os.chdir(os.path.dirname(os.path.abspath(__file__))) # 현재 실행 중인 파일의 폴더로 작업 디렉토리 변경
sys.stdin = open("swea_input.txt", "r") # 표준 입력을 파일로 변경
input = sys.stdin.readline



def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # 경로 압축
    return parent[x]
 
def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA != rootB:  # 서로 다른 집합이면 합침
        parent[rootB] = rootA  # B의 루트를 A로 변경
 
T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 사람 수 N, 관계 수 M
    parent = list(range(N + 1))  # 각 노드의 부모를 자기 자신으로 초기화
 
    for _ in range(M):
        a, b = map(int, input().split())  # a와 b가 연결됨
        union(parent, a, b)
 
    # 모든 노드의 최종 대표(parent)를 찾아 중복 제거 후 개수 세기
    groups = set(find(parent, i) for i in range(1, N + 1))
    print("idx:   ", [i for i in range(N+1)])
    print("parent", parent)
    print(f"#{tc} {len(groups)}")