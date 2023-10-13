# (0, 0) -> (n-1, m-1)
from collections import deque

def solution(graph):
    n, m = len(graph), len(graph[0])
    queue = deque([(0, 0)])
    # graph[0][0] = 100
    drdc = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        row, col = queue.popleft()
        base_cnt = graph[row][col]
        print(f"> ({row}, {col})")

        for d in drdc:
            dr, dc = d
            nr = row + dr
            nc = col + dc

            if nr < 0 or nc < 0 or nr >= n or nc >= m or base_cnt == 0:
                continue

            if graph[nr][nc] == 1:
                graph[nr][nc] += base_cnt
                queue.append((nr, nc))

            if (nr, nc) == (n-1, m-1):
                return graph[nr][nc]
            
            


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[int(i) for i in list(input())]  for _ in range(n)]

    print(solution(graph))