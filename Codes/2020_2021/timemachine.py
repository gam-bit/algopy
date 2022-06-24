# https://www.acmicpc.net/problem/11657
# ssp(single source shortest path) 단일 출발지 최단 경로
# 벨만포드 알고리즘
    ## 1. n개의 노드를 가진 그래프에서 최단거리는 최대 n-1개의 간선을 이동 >> n-1번 간선을 돌면서 움직임
        ## >> 이동했던 곳을 다시 이동해서 최단거리가 나오면 negative cycle이 생긴 것
    ## 2. Relaxing : 간선을 돌면서 '현 단계의 next_node의 distance < 이전 단계의 next_node의 distance' -> distance 변경
    ## 3. n번째 단계에서도 relaxing이 작동하면 negative cycle이 존재함 -> return False
    


def bf(start):

    dist[0] = 0 # 0은 없음
    dist[start] = 0

    for k in range(n): # n-1번 모든 간선 확인
        
        for i in range(m):
            v_cur, v_next, cost = path[i]
            
            # relaxing
            if (dist[v_next] > dist[v_cur] + cost) and (dist[v_cur] != inf):
                                                    ## dist[v_cur] != inf 
                                                    ## 이 조건이 있어야 출발점에서 연결된 경로를 찾게 됨 
                                        
                dist[v_next] = dist[v_cur] + cost
            
                if k == n-1: # n번 확인했을 때 최단거리가 업데이트되면 negative cycle이 존재
                    return False

    for i in range(n+1): # 각 노드의 dist 확인
        if dist[i] == inf:
            dist[i] = -1
   
    return True



if __name__ == '__main__':
    n, m = map(int, input().split()) # 노드, 간선 수
    path = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        path.append((a, b, c))

    inf = int(1e9)
    dist = [inf] * (n+1) # 0은 없음
      
    start = 1 # 1번 도시에서 출발
    print('bf:', bf(start))
    # if bf(start):
    #     del dist[start]
    #     for i in dist[1:]:
    #         print(i)
    # else:
    #     print(-1)


                
