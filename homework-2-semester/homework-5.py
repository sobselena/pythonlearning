def DFS(adj_list, curr_el = 0,  visited=None):
    if visited is None:
        visited = set()
    print(f"Входим в вершину {curr_el + 1}")
    visited.add(curr_el)

    for el in adj_list[curr_el]:
        if el not in visited:
            DFS(adj_list, el, visited)

    print(f"Выходим из вершины { curr_el + 1}")

N, M = map(int, input().split())

adj_list = [[] for i in range(N)]

for i in range(M):
    v, u = map(int, input().split())
    adj_list[v-1].append(u-1)
    adj_list[u-1].append(v-1)

DFS(adj_list)