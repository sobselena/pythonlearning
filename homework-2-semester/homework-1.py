N, M = map(int, input().split())
edges = []
for i in range(M):
    edges.append(list(map(int, input().split())))
print(edges)
for edge in edges:
    print(edge)