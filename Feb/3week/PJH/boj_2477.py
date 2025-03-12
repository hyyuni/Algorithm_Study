K = int(input())
list_cham = [list(map(int,input().split())) for _ in range(6)]
list_dir = []
list_len = []
for i in range(6):
    list_dir.append(list_cham[i][0])
    list_len.append(list_cham[i][1])
index_dir = []
for a in list_dir:
    if list_dir.count(a)==1:
        index_dir.append(list_dir.index(a))

if index_dir[1] - index_dir[0] == 1:
    a_c = K*((list_len[index_dir[0]-1]*list_len[index_dir[0]-2])+(list_len[index_dir[1]]*list_len[(index_dir[1]+1)%6]))
else:
    a_c = K*((list_len[index_dir[0]]*list_len[index_dir[0]+1])+(list_len[index_dir[1]-1]*list_len[index_dir[1]-2]))

print(a_c)
