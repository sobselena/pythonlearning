A = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]

A_reversed = [[0] * len(A) for i in range(len(A))]
for i in range(len(A)):
    for j in range(len(A)):
        A_reversed[j][i] = A[i][j]
for el in A_reversed:
    print(*el)