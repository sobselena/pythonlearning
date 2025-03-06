N = int(input())
edge_list = [[1, 2], [2, 3], [3, 4], [4, 1]]
A = [[0] * N for i in range(N)]
for v, u in edge_list:
    A[v-1][u-1] = 1
    
for el in A:
    print(*el)