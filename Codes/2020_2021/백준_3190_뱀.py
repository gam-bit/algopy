# https://www.acmicpc.net/problem/3190


n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
apple_loc = [] # 사과 위치
change_direc = {} # 방향 전환 시간 
                  # {'3': 'D', "17":'L'}

for _ in range(k):
    a, b = map(int, input().split())
    apple_loc.append((a, b)) 
    
m = int(input()) # 방향 전환 횟수
for _ in range(m):
    sec, direc = input().split()
    change_direc[sec] = direc
change_sec = list(map(int, change_direc.keys())) # 방향 바뀌는 초 list [3, 17, 18]

direc = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 오른쪽, 아래, 왼쪽, 위 
direc_idx = 0
snake = [(1, 1)] 

# 목표) 게임이 몇 초 뒤에 끝나는지 출력

# 1. 뱀이 이동할 자리에 사과 or 뱀/벽이 있나 확인
# 1-(1). 뱀 or 벽이 있나 확인
    ## 있으면 -> 게임 종료
# 1-(2). 사과가 있나 확인
    ## 있으면 -> 뱀 늘리기, 사과 없애기
    ## 없으면 -> 뱀 이동하기
# 2. 방향 전환 확인하기


t = 0

while True:
    t += 1

    # 1. 뱀이 이동할 위치에 사과 or 뱀/벽이 있나 확인
    x, y = tuple(map(sum, zip(snake[len(snake)-1], direc[direc_idx]))) # 이동할 위치
    # 1-(1) 뱀 or 벽 있나 확인
    if (x < 1) | (y < 1) | (x > n) | (y > n) | ((x, y) in snake):
        break
    
    # 1-(2) 사과있나 확인 -> 뱀 이동시키기
    if (x, y) in apple_loc:
        print('뱀 사과먹는다')
        snake.append((x, y)) # 뱀 머리 늘리기 [(1, 1), (1, 2)]
        apple_loc.remove((x, y)) # 사과 없애기 
    else:
        snake[:len(snake)-1] = snake[1:] 
        snake[len(snake)-1]  = (x, y)

    print(f"{t}초")
    print(f"snake: {snake}")
    
    
    # 방향 전환
    if t in change_sec: 
        if change_direc[str(t)] == 'L':
            direc_idx = (direc_idx - 1) % 4
            print(f"{t}초에 왼쪽으로 방향전환-{direc[direc_idx]}")
        else:
            direc_idx = (direc_idx + 1) % 4
            print(f"{t}초에 오른쪽으로 방향전환-{direc[direc_idx]}")
    

    print('-'*10)


print(t)
