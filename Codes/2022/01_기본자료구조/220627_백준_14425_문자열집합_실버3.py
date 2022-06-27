# 자료구조
# https://www.acmicpc.net/problem/14425

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

S = set([input() for i in range(n)])

cnt = 0
for j in range(m):
    word = input()
    if word in S:
        cnt += 1

print(cnt)