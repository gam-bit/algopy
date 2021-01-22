# https://www.acmicpc.net/problem/2252
from collections import deque


def topo_sort(n, indegree, graph):

    results = []
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        results.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    print(' '.join([str(i) for i in results]))


if __name__ == '__main__':

    n, m = map(int, input().split())
    # 학생 번호 1-n번
    # m 가지 경우를 줌
    # 줄세우기 
    # 답여러개면 아무거나 출력
    graph = [[] for i in range(n+1)]
    indegree = [0] * (n+1)

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    topo_sort(n, indegree, graph)

