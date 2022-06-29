# 자료구조 - 힙
# https://www.acmicpc.net/problem/2696

import heapq
import sys
input = sys.stdin.readline

def median(heap):
    heapq.heapify(heap)
    n = len(heap)
    n_rm = int((n-1)/2)
    
    for _ in range(n_rm):
        heapq.heappop(heap)
    
    return heapq.heappop(heap)
        

if __name__ == "__main__":
    t = int(input())

    for i in range(t):
        seq = []
        medians = []
        m = int(input())
        while m > len(seq):
            seq += list(map(int, input().split()))
        for k in range(len(seq)):
            if k % 2 == 0:
                heap = seq[:k+1].copy()
                medians.append(median(heap))
        # 10개씩 출력
        print(len(medians))
        for i in range(0, len(medians), 10):
            print(" ".join([str(i) for i in medians[i:i+10]]))
