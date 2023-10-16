# https://www.acmicpc.net/problem/14503
# <작동을 멈출 때까지 청소 영역 개수 구하기> 

# 방 n x m 직사각형
# 0 : 청소 X 빈 칸 / 1 : 벽 / -1 : 청소된 빈칸
# 현재칸 청소 
    ## -> 주변에 빈 칸이 없으면 후진
    ## -> 빈 칸이 있으면 반시계방향으로 90도씩 돌면서 빈 칸으로 이동
from collections import deque

drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북동남서(0123) -> 1씩 커지면 시계방향. 1씩 작아지면 반시계방향
                                                # +!, -1하고 4로 나눈 나머지 구하면 됨


n, m = map(int, input().split())
r, c, d = map(int, input().split()) # (r, c) => 로봇 청소기 위치, d = 방향
room = [[int(v) for v in input().split()] for _ in range(n)]

cnt_clean = 0

queue = deque([(d-i-1)%4 for i in range(4)])
while queue:
    
    # 1. 현재 칸 청소
    if room[r][c] == 0:
        cnt_clean += 1
        room[r][c] = -1

    # 2. 이동
    d = queue.popleft()
    dr, dc = drdc[d]
    nr, nc = r+dr, c+dc # 이동 후 로봇 위치
    if nr < 0 or nc < 0 or nr >= n or nc >= m:
        continue

    if room[nr][nc] == 0:
        queue = deque([(d-i-1)%4 for i in range(4)]) # 이동할 경우, queue 갱신
        r, c = nr, nc
    
    # 3. 이동할 수 있는 곳이 없을 때
    if not queue:
        d = (d+2) % 4
        dr, dc = drdc[d]
        nr, nc = r+dr, c+dc # 후진 후 로봇 위치
        if room[nr][nc] != 1:
            r, c = nr, nc
            d = (d+2) % 4
            queue = deque([(d-i-1)%4 for i in range(4)]) 


print(cnt_clean)
