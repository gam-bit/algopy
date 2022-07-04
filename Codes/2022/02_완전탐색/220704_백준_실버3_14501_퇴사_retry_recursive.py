# https://www.acmicpc.net/problem/14501

import sys
input = sys.stdin.readline

def recursive(n, t_list, p_list, idx, cumsum=0):
    global result
    # 탈출 조건
    if idx == n:
        result = max(result, cumsum)
        return
    # 상담 안 함        
    recursive(n, t_list, p_list, idx+1, cumsum)

    # 상담을 함 
    if idx + t_list[idx] > n:
        return
    cumsum += p_list[idx]
    idx += t_list[idx]
    recursive(n, t_list, p_list, idx, cumsum)
 
if __name__ == "__main__":
    n = int(input())
    t_list = []
    p_list = []

    for i in range(n):
        t, p = map(int, input().split())
        t_list.append(t)
        p_list.append(p)

    result = 0
    recursive(n, t_list, p_list, 0, 0)
    print(result)

                
"""
- 상담할 때와 하지 않을 때 2가지 경우로 재귀를 돌려야하므로 return에 함수를 넣을 수 없음 
  -> global variable 사용
"""