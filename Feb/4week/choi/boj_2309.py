from itertools import combinations

def find(combi, arr):
    for i in combi:
        for j in i:
            arr.append(j)
        if sum(arr) == 100:
            result = sorted(arr) 
            return result
        else:
            arr.clear()
    

height = [int(input()) for _ in range(9)]
combi = list(combinations(height,7))
# sum_hei = sum(height)
# minus = sum_hei - 100
arr = []
real = find(combi, arr)
for i in real:
    print(i)