# https://www.acmicpc.net/problem/11651

import sys
input = sys.stdin.readline

n = int(input())

coord_list = []
for _ in range(n):
    coord = list(map(int, input().split()))
    coord_list.append(coord)
    
coord_list = sorted(coord_list, key=lambda x: (x[1], x[0]))

for coord in coord_list:
    x, y = coord
    print(x, y)