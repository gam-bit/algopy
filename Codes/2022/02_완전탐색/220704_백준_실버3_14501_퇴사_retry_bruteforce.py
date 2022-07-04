# https://www.acmicpc.net/problem/14501

from collections import deque
import copy
import sys
input = sys.stdin.readline


def brute_force(n, t_list, p_list):
    result = 0
    queue = deque()
    queue.append(([0 for _ in range(n)], 0))
    
    while queue:
        arr, idx = queue.popleft()
        
        # 마지막 날짜까지 다 간 경우
        if idx < n:
            result = max(result, sum(arr))
        
        else:
            # 상담을 안 함
            queue.append((copy.deepcopy(arr), idx+1))

            # 상담을 함
            if idx + t_list[idx] <= n:
                arr[idx] = p_list[idx]
                idx += t_list[idx]
                queue.append((copy.deepcopy(arr), idx))
            result = max(result, sum(arr))
                
    return result



if __name__ == "__main__":
    n = int(input())
    t_list = []
    p_list = []

    for i in range(n):
        t, p = map(int, input().split())
        t_list.append(t)
        p_list.append(p)

    print(brute_force(n, t_list, p_list))

                
            