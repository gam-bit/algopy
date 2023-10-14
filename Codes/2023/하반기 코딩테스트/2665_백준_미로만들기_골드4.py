# # bfs
# # https://www.acmicpc.net/problem/2665
import sys
import heapq

# input = sys.stdin.readline

def bfs(graph):
    heap = []
    heapq.heappush(heap, (0, 0, 0)) # (cnt, row, col)

    drdc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    n = len(graph)
    visited = [[False]*n for _ in range(n)]

    while heap:

        cnt, row, col = heapq.heappop(heap)
        
        if row==n-1 and col==n-1:
            return cnt

        for dr, dc in drdc:
            nr = row+dr
            nc = col+dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:

                if graph[nr][nc] == 1: # 열린 길
                    visited[nr][nc] = True
                    heapq.heappush(heap, (cnt, nr, nc))

                elif graph[nr][nc] == 0: # 막힌 길
                    visited[nr][nc] = True
                    heapq.heappush(heap, (cnt+1, nr, nc))


if __name__ == "__main__":
    n = int(input())
    graph = [[int(i) for i in list(input())] for _ in range(n)]


    print(bfs(graph))



