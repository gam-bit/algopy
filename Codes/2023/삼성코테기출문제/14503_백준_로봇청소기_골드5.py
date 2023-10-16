# https://www.acmicpc.net/problem/14503
# <청소 영역 개수 구하기>

# 방 n x m 직사각형
# 0 : 청소 X 빈 칸 / 1 : 벽
# 현재칸 청소 
    ## -> 주변에 빈 칸이 없으면 후진
    ## -> 빈 칸이 있으면 빈 칸으로 이동


drdc = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북동남서(0123)

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # (r, c) => 로봇 청소기 위치, d = 방향
room = [[int(v) for v in input().split()] for _ in range(n)]

cnt_clean = 0


