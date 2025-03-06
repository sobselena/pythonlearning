def BFS(start, adj_list, visited):
    visited.add(start)
    queue = [start]

    while queue:
        curr_el = queue.pop(0)
        for el in adj_list[curr_el]:
            if el not in visited:
                visited.add(el)
                queue.append(el)   
    return visited

def comp_count(adj_list):
    visited = set()
    k = 0
    
    for i in range(len(adj_list)):
        if i not in visited:
            BFS(i, adj_list, visited)
            k += 1
    return k

N, M = map(int, input().split())

adj_list = [[] for i in range(N)]

for i in range(M):
    v, u = map(int, input().split())
    adj_list[v-1].append(u-1)
    adj_list[u-1].append(v-1)

print(comp_count(adj_list))