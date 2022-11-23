# https://www.acmicpc.net/problem/13549
"""
- 노드간 가중치가 일정하지 않아서 일반적으로는 다익스트라 알고리즘을 사용하지만,
그렇다고 bfs를 사용하지 못하는 것은 아님.
- 0-1 bfs를 활용 -> 가중치가 0일 때는 appendleft로 앞 단에 추가하면 됨
"""

import sys
from collections import deque

def solution1(n, k):
    "경로를 남기는 방법. but 시간초과^^"
    MAX_NUM = 100001
    check = [-1] * MAX_NUM
    q = deque()
    q.append([n])
    check[n] = 0

    while q:
        pos_list = q.popleft() 
        last_pos = pos_list[-1]

        if last_pos == k:
            # print(pos_list)
            return check[last_pos]
        
        for new_pos in [last_pos-1, last_pos+1, last_pos*2]:
            if 0 <= new_pos < MAX_NUM and check[new_pos] == -1:
                if new_pos == last_pos*2:
                    q.appendleft(pos_list+[new_pos])
                    check[new_pos] = check[last_pos]
                else:
                    q.append(pos_list+[new_pos])
                    check[new_pos] = check[last_pos]+1


def solution(n, k):
    MAX_NUM = 100001
    check = [-1] * MAX_NUM
    q = deque()
    
    q.append(n)
    check[n] = 0

    while q:
        pos = q.popleft() 

        if pos == k:
            return check[pos]
        
        for new_pos in [pos-1, pos+1, pos*2]:
            if 0 <= new_pos <  MAX_NUM and check[new_pos] == -1:
                if new_pos == pos*2:
                    q.appendleft(new_pos)
                    check[new_pos] = check[pos]
                else:
                    q.append(new_pos)
                    check[new_pos] = check[pos]+1


if __name__=='__main__':
    sys.setrecursionlimit(50000)
    input = sys.stdin.readline
    n, k = map(int, input().split())
    print(solution(n, k))