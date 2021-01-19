# https://www.acmicpc.net/problem/4386

import math

def dist_stars(star_loc, a, b):
    
    diff_x = star_loc[a][0] - star_loc[b][0]
    diff_y = star_loc[a][1] - star_loc[b][1]

    return math.sqrt(diff_x**2 + diff_y**2)


def find_parents(parents, x):
    if x != parents[x]:
        parents[x] = find_parents(parents, parents[x])
    
    return parents[x]


def union_parents(paretns, a, b):
    par_a = find_parents(parents, a)
    par_b = find_parents(parents, b)

    if par_a < par_b:
        parents[par_b] = par_a
    else:
        parents[par_a] = par_b


if __name__ == "__main__":

    n = int(input()) # 별 개수 (1번 ~ n번 별)

    parents = [i for i in range(n+1)]

    star_loc = [[] for i in range(n+1)] # 별 좌표
    for i in range(1, n+1):
        x, y = map(float, input().split())
        star_loc[i] = [x, y]

    edges = []
    for i in range(1, n):
        for j in range(i+1, n+1):
            dist = dist_stars(star_loc, i, j)
            edges.append((dist, i, j))


    edges.sort() # 거리가 가까운 edges 순서로 나열

    total_dist = 0
    path = []
    for e in edges:
        c, a, b = e

        if find_parents(parents, a) != find_parents(parents, b):
            union_parents(parents, a, b)
            total_dist += c
            path.append(e)


    print(round(total_dist, 2))