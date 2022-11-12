def dfs(graph, v, visited):
    "재귀 사용"
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def dfs_stack(graph, start_node=1):
    "stack 사용"
    stack = [start_node]
    hist = set([start_node])
    while stack:
        pop_node = stack.pop()
        print(pop_node)
        stack += sorted([i for i in graph[pop_node] if i not in hist], reverse=True)
        hist = set(list(hist) + stack)
        


if __name__ == "__main__":
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7], 
        [2, 6, 8],
        [1, 7]
    ]  # 1 2 7 6 8 3 4 5

    # visited = [False for _ in range(len(graph))]
    # dfs(graph, 1, visited)

    dfs_stack(graph)
    