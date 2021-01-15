# <커리큘럼 문제>
# 위상정렬
"""
> input :
5 (과목수)
10 -1 (이수해야하는 시간, 사전이수과목들..., -1)
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1
> output :
10
20
14
18
"""

from collections import deque

import sys
input = sys.stdin.readline


def t_sort(n, idegree, graph, time):
    inf = int(1e9)
    time_results = [inf] * (n+1)
    q = deque()
    
    for i in range(1, n+1):
        if idegree[i] == 0:
            q.append(i)
            time_results[i] = time[i]

    while q:
        now = q.popleft()
        for i in graph[now]: 
            idegree[i] -= 1
            if idegree[i] == 0:
                q.append(i)
                
                # 제일 적게 걸리는 경로의 시간을 결과로 추출
                cur_path_time = time_results[now] + time[i]
                if time_results[i] > cur_path_time:
                    time_results[i] = cur_path_time

    return time_results 



        
if __name__ == '__main__':
    n = int(input())

    idegree = [0] * (n+1)
    graph = [[] for i in range(n+1)]
    time = [0] * (n+1)
    for i in range(1, n+1):
        input_lst = list(map(int, input().split()))
        last_idx = input_lst.index(-1)
        time[i] = input_lst[0]
        if last_idx != 1:
            idegree[i] = len(input_lst[1:last_idx])
            for j in input_lst[1:last_idx]:
                graph[j].append(i)
            
        else:
            idegree[i] = 0


    results = t_sort(n, idegree, graph, time)

    for i in results[1:]:
        print(i)
