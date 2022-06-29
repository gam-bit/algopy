# 자료구조 - 힙
# https://www.acmicpc.net/problem/2075
# 메모리 주의

import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = list(map(int, input().split()))

for _ in range(n-1):
    minval = min(heap)
    candis = list(map(int, input().split()))
    
    for i in candis:
        if i > minval:
            heapq.heappush(heap, i)
            heapq.heappop(heap)
            
print(heap[0])


"""
* 참고 자료에 해결 방법 있음
    - input값이 하나씩 들어올 때마다 최소값 버리기
    - 길이가 n인 힙을 만들어서 최소값 배출하면 됨
    - push 전에 pop을 먼저하면 heapify하지 않고 바로 첫번째 인자를 배출해버림
        -> push부터 수행
"""