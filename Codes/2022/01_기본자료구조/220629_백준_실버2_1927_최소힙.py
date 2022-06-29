# 자료구조 - 힙
# https://www.acmicpc.net/problem/1927

import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    k = int(input())
    if k == 0:
        if heap:
            popval = heapq.heappop(heap)
        else:
            popval = 0
        print(popval)
    else:
        heapq.heappush(heap, k)


"""
cf.) 최대힙을 구할 때엔 원소에 -1을 곱해서 처리하면 됨
"""