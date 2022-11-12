from collections import deque

def bfs(graph, start_node=1):
    queue = deque([start_node])
    hist = set([start_node])
    while queue:
        pop_node = queue.popleft()
        print(pop_node)
        queue += deque([i for i in graph[pop_node] if i not in hist])
        hist = set(list(hist) + list(queue))


if __name__ == "__main__":
    # input
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
    ]  # 1 2 3 8 7 4 5 6

    bfs(graph)