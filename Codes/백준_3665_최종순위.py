# https://www.acmicpc.net/problem/3665

from collections import deque


def topo_sort(n, graph, indegree):
    # indegree에 0이 2번 나오는 상황 -> '?'
    # 진입차수가 다 0인 상황이 안 나올 때 -> 'IMPOSSIBLE'

    results = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:

        now = q.popleft()
        results.append(now)

        for i in graph[now]: # now의 목적지 확인
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    print(' '.join([str(i) for i in results]))


# 입력
n = int(input()) # n팀
last_rank = list(map(int, input().split())) # 작년 순위
m = int(input()) # 올해 등수가 바뀐 경우
shift_case = []
for _ in range(m):
    a, b = map(int, input().split())
    shift_case.append((a, b))

# sort를 위한 데이터
indegree = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(n-1):
    now = last_rank[i]
    
    for j in range(i+1, n): 
        ahead = last_rank[j]
        graph[now].append(ahead) 
        indegree[ahead] += 1


while shift_case:
  
    a, b = shift_case.pop()


    if b in graph[a]: # a -> b 이면 b -> a로 변경
        indegree[b] -= 1
        indegree[a] += 1
        graph[a].remove(b)
        graph[b].append(a)

    elif a in graph[b]:
        indegree[a] -= 1
        indegree[b] += 1
        graph[b].remove(a)
        graph[a].append(b)


    print(f"shift_case: ({a, b})")
    print(graph)
    print(indegree)
    print('-'*30)


topo_sort(n, graph, indegree)
    