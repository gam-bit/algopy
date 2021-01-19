# https://www.acmicpc.net/problem/9372




# 방법1) 크루스칼 알고리즘

import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline

def find_parents(parents, x):
    if x != parents[x]:
        parents[x] = find_parents(parents, parents[x])

    return parents[x]



def union_parents(parents, a, b):
    par_a = find_parents(parents, a)
    par_b = find_parents(parents, b)

    if par_a < par_b:
        parents[par_b] = par_a
    else:
        parents[par_a] = par_b




t = int(input())

results = []
for _ in range(t):
    n, m = map(int, input().split()) # n: 국가, m: 비행기 
    
    parents = [i for i in range(n+1)]
    edges = []
    for i in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))
        
    c = 0
    for e in edges:
        a, b = e
        
        if find_parents(parents, a) != find_parents(parents, b):
            union_parents(parents, a, b)
            c += 1
        
    results.append(c)


for i in results:
    print(i)
            


#-------------------

# 방법2) n-1
import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline


t = int(input())

for _ in range(t):
    n, m = map(int, input().split()) # n: 국가, m: 비행기 

    for i in range(m):
        a, b = map(int, input().split())
        
    print(n-1)
