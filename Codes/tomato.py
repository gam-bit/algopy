# https://www.acmicpc.net/problem/7576
# BFS

from collections import deque


def find_idx_ripe_tomato(tomatobox):
    tomato_idx = []
    for r in range(len(tomatobox)):
        for c in range(len(tomatobox[0])):
            if tomatobox[r][c] == 1:
                tomato_idx.append((r, c))
    return tomato_idx


def solution(tomatobox):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    
   
    q = deque(find_idx_ripe_tomato(tomatobox)) 
    
    while q:
        r, c = q.popleft()
        
        for dr, dc in move:
            i, j = r+dr, c+dc
            
            if (i < 0) | (j < 0) | (i >= n) | (j >= m):
                continue
            
            elif tomatobox[i][j] == 0:
                tomatobox[i][j] = tomatobox[r][c] + 1
                q.append((i, j))
    
    cnt_lst = []             
    for lst in tomatobox:
        cnt_lst += lst
    
    if 0 in cnt_lst:
        return -1 

    return max(cnt_lst) - 1
        

if __name__ == '__main__':
    m, n = map(int, input().split()) # 가로, 세로

    tomatobox = []
    for _ in range(n):
        tomatobox.append(list(map(int, input().split())))

    print(solution(tomatobox))
           
        
                

