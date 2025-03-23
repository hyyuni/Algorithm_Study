class SegmentTreeBottomUp:
    def __init__(self, leaf_nodes):
        self.n = len(leaf_nodes)
        self.tree = [0]*(2*self.n)
        self.tree[self.n:] = leaf_nodes[:]
        self.build()
        # 전파를 누적해서 저장할 예정
        self.lazy = [0]*(2*self.n)
        # 각 노드가 담당하는 구간의 길이를 저장
        self.seg_len = [0]*(2*self.n)
        self.seg_len[self.n:] = [1]*self.n
        for i in range(self.n-1, 0, -1):
            self.seg_len[i] = self.seg_len[2*i] + self.seg_len[2*i+1]
    
    def plus(self, a, b):
        return a+b
    
    def build(self):
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.plus(self.tree[2*i], self.tree[2*i+1])

    def _push(self, idx):
        """
        lazy[idx]를 자식에게 전파(push down)하고, idx의 lazy는 비운다.
        (idx가 리프면 아무 일도 안 함)
        """
        if self.lazy[idx] != 0:
            # 왼쪽 자식
            lch = idx * 2
            self.lazy[lch] += self.lazy[idx]
            self.tree[lch] += self.lazy[idx] * self.seg_len[lch]
            
            # 오른쪽 자식
            rch = lch + 1
            self.lazy[rch] += self.lazy[idx]
            self.tree[rch] += self.lazy[idx] * self.seg_len[rch]
            
            # 본인 lazy는 0으로
            self.lazy[idx] = 0

    def _pull(self, idx):
        """
        자식의 tree 값을 합쳐서 idx의 tree를 갱신
        (lazy[idx]도 고려해야 하지만, 이미 자식으로부터 tree 값이 반영된 뒤라
         여기서는 단순 합으로도 일관성 유지)
        """
        self.tree[idx] = self.plus(
            self.tree[idx * 2],
            self.tree[idx * 2 + 1]
        ) + self.lazy[idx] * self.seg_len[idx]

    def _push_path(self, x):
        """
        루트(1)에서 x로 가는 경로 상에 있는 노드들을
        위에서부터 순서대로 push(전파)한다.

        => x가 리프 인덱스(>= n)일 수도 있지만, 내부 인덱스(< n)일 수도 있다.
           경로에 존재하는 모든 부모 노드를 윗단부터 push해서 
           최종적으로 x의 조상들이 미룬 lazy가 전부 아래로 내려가도록 한다.
        """
        path = []
        cur = x // 2
        while cur > 0:
            path.append(cur)
            cur //= 2
        
        # 루트에서부터 내려오며 push
        for node in reversed(path):
            self._push(node)

    def _pull_path(self, x):
        """
        x에서 루트(1)까지 올라가며 pull(자식 합)을 갱신.
        """
        cur = x // 2
        while cur > 0:
            self._pull(cur)
            cur //= 2

    def update_apply(self):
        # 루트부터 내부 노드(인덱스 1 ~ n-1)까지 lazy 업데이트를 자식으로 전파
        for i in range(1, self.n):
            if self.lazy[i] != 0:
                # 자식 노드에 lazy 값 누적
                self.lazy[2*i] += self.lazy[i]
                self.lazy[2*i+1] += self.lazy[i]
                # 자식 노드의 tree 값에도 lazy 반영 (구간 길이 만큼 곱해 더함)
                self.tree[2*i] += self.lazy[i] * self.seg_len[2*i]
                self.tree[2*i+1] += self.lazy[i] * self.seg_len[2*i+1]
                self.lazy[i] = 0
    
    
    def update_range(self, left, right, val):
        """
        구간 [left, right]에 val을 더한다 (BOJ 10999에서 요구하는 연산)
        => 바텀업 + lazy (iterative) 방식.
        """
        left += self.n
        right += self.n
        
        l0, r0 = left, right
        
        # 1) left와 right의 경로에 있는 노드들만 push하여
        #    현재까지 남아 있던 lazy를 리프 쪽에 미리 반영해둔다.
        self._push_path(left)
        self._push_path(right)
        
        # 2) [left, right] 범위의 노드들에 업데이트
        while left <= right:
            if (left % 2) == 1:   # left가 홀수
                self.lazy[left] += val
                self.tree[left] += val * self.seg_len[left]
                left += 1
            if (right % 2) == 0: # right가 짝수
                self.lazy[right] += val
                self.tree[right] += val * self.seg_len[right]
                right -= 1
            left //= 2
            right //= 2
        
        # 3) 업데이트가 끝난 뒤, l0, r0를 부모 방향으로 pull해 
        #    상위 노드들의 구간합을 다시 갱신
        self._pull_path(l0)
        self._pull_path(r0)
    
    def query(self, left, right):
        """
        구간 [left, right] 합을 구하기.
        => 쿼리 시에도 부분 경로의 lazy를 push_path로 내려서
           정확한 값(특히 리프)을 가져오도록 해야 한다.
        """
        left += self.n
        right += self.n
        
        # 1) 쿼리 구간 양끝의 경로에 있던 lazy를 자식에게 미리 반영
        self._push_path(left)
        self._push_path(right)
        
        # 2) 이제 표준적인 바텀업 구간 합 쿼리
        result = 0
        while left <= right:
            if (left % 2) == 1:
                result = self.plus(result, self.tree[left])
                left += 1
            if (right % 2) == 0:
                result = self.plus(result, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return result

N, M, K = map(int,input().split())

leaf_nodes = []
for _ in range(N):
    leaf_nodes.append(int(input()))
tree = SegmentTreeBottomUp(leaf_nodes)

for _ in range(M+K):
    order = list(map(int,input().split()))
    order_num = order[0]
    # idx화 하려면 -1 해야한다. 번째의 의미
    start = order[1]-1
    end = order[2]-1
    if order_num == 1:
        d = order[3]
        tree.update_range(start, end, d)
    if order_num == 2:
        print(tree.query(start, end))
