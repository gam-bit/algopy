from collections import deque

def solution(maze):
    
    def bfs(y, x):
        q = deque()
        q.append((y, x, 1))
        while q:
            b, a, dist = q.popleft()
            
            if b == len(maze)-1 and a == len(maze[0]) -1:
                return dist

            if maze[b][a] == 0:
                continue

            maze[b][a] = 0
            
            if b+1 < len(maze):
                q.append((b+1, a, dist+1))
            if a+1 < len(maze[0]):
                q.append((b, a+1, dist+1))
            if b-1 >= 0:
                q.append((b-1, a, dist+1))
            if a-1 >= 0:
                q.append((b, a-1, dist+1))
            
        return -1
    
    return bfs(0, 0)


def solution2(maze):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    q = deque()
    q.append((0, 0, 1))
    
    while q:
        y, x, dist = q.popleft()
        
        if y == len(maze)-1 and x == len(maze[0])-1:
            return dist

        for dy, dx in move:
            j, i = y+dy, x+dx 

            if 0 <= j < len(maze) and 0 <= i < len(maze[0]):
                if maze[j][i] != 0:
                    q.append((j, i, dist+1))
                    maze[j][i] = 0 
        
    return -1



if __name__=="__main__":
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, list(input()))))
    # print(maze)
    # print(f"maze size: ({len(maze)}, {len(maze[0])})")
    print(solution2(maze))