# https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""
bfs로 미로 최단거리 문제를 푸는 이유:
breadth 방향으로 탐색하면서 이미 지나갔던 길은 지나가지 않게 만들기 때문에
같은 위치를 먼저 도착하는 경로로 이동하게 되기 때문
"""
from collections import deque

def solution(maps):
    def bfs(y, x):
        q = deque()
        q.append((y, x, 1))
        
        while q:
            y, x, distance = q.popleft()    
            if y == len(maps)-1 and x == len(maps[0])-1:
                return distance
            
            if maps[y][x] == 0:
                continue
            maps[y][x] = 0
            
            if y+1 < len(maps):
                q.append((y+1, x, distance+1))
            if y-1 >= 0:
                q.append((y-1, x, distance+1))
            if x+1 < len(maps[0]):
                q.append((y, x+1, distance+1))
            if x-1 >= 0:
                q.append((y, x-1, distance+1))
        return -1
    return bfs(0, 0)


if __name__=="__main__":
    maps = [[1,0,1,1,1],
            [1,0,1,0,1],
            [1,0,1,1,1],
            [1,1,1,0,1],
            [0,0,0,0,1]] # 11
    # maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]] # -1
    print(solution(maps))
    # print(maps[1][0])