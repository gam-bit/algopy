## <미로 찾기>
## 2020-12-27
## 난이도 1.5
## 풀이시간 30분
## 시간 제한 1초 | 메모리 제한 128MB

## sol
## <input>
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
## <output>
## 10

#----------------------------------------

# 상하좌우로 움직일 수 있음
# 0이면 이동 불가능, 1이면 이동 가능
# bfs -> 큐 사용

from collections import deque



# n x m 미로 생성
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))



def solution(maze, n, m):
    
    q = deque([(0, 0)]) # 출발점 
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    
    while q:
        r, c = q.popleft() # 현 위치


        for dr, dc in move: # 현 위치에서 인접한 곳에 길이 있는지 파악하기
            
            i = r+dr
            j = c+dc

            if (i >= n) | (j >= m) | (i < 0) | (j < 0): # 미로를 벗어난 경우
                continue
            
            elif maze[i][j] == 1: # 길이 있는 경우
                q.append((i, j))  # 해당 인덱스를 큐에 추가
                maze[i][j] = maze[r][c] + 1 # 인덱스를 추가하면서 거리 추가

    # print(maze)
    return maze[n-1][m-1] # 마지막 위치까지 이동한 거리


print(solution(maze, n, m))