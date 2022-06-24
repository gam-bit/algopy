## <게임 개발>
## 2020-12-25
## 난이도 2
## 풀이시간 40분
## 시간 제한 1초 | 메모리 제한 128MB

n, m = map(int, input('세로 가로 : ').split()) # n: 세로, m: 가로 -- 3이상 50이하
a, b, d = map(int, input('현재 위치(a b d) : ').split()) # 현재 위치(d는 바라보는 방향)
                                                        # 0: 북, 1: 동, 2:남, 3:서
                                                        
game_map = []
for i in range(n):
    game_map.append(list(map(int, input().split())))


#-------------------------------------------------

# 0: 육지, 1: 바다, 2: 지나갔던 곳
moved_map = []
for i in range(n):
	moved_map.append(['No' for j in range(m)])
    ###########################################
    # 주의 )                                  #
    # moved_map = [['No'] * m ] * n으로 하면  # 
    # 안쪽에 있는                             #
    # ['No', 'No', No', ...], ...        들이 #
    # shallow copy되어서 같이 바뀌어버림!!!    #
    # 그러므로 위와 같이 생성해야 함           #
    ##########################################

    
move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서


moved_map[a][b] = 'Yes'
game_map[a][b] = 2
cnt = 1 # 지나간 칸의 수

while True:
    rot = 0 # 방향 전환
    

    for i in range(4):

        d = (d-1) % 4  ## 왼쪽 방향부터 보기
        m, n = move[d] ## 이동 방법
        
        if game_map[a+m][b+n] == 0: # 육지일 때
            a += m
            b += n
            game_map[a][b] = 2
            moved_map[a][b] = 'Yes'
            cnt += 1
            break

        else: # 육지가 아닐 때 == 바다거나 지나간 곳일 때
            rot += 1
        
        

    # 상하좌우 다 봤는데 움직일 곳이 없다면
    if rot == 4:

        m, n = move[(d+2) % 4]
        
        if game_map[a+m][b+n] == 2:
            a += m
            b += n
        else:
            break

    print(game_map)  
    

print(moved_map) 
print(cnt)

