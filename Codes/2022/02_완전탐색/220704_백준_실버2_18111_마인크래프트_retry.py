# brute force -> 시간초과
# https://www.acmicpc.net/problem/18111

import sys
input = sys.stdin.readline

def add(h_now, h, result, remain_b):
    result += (h-h_now) 
    remain_b -= (h-h_now)
    return result, remain_b
    

def extract(h_now, h, result, remain_b):
    result += (h_now - h) * 2
    remain_b += (h_now - h)
    return result, remain_b

if __name__ == "__main__":

    N, M, B = map(int, input().split())
    total_space = []

    for _ in range(N):
        space = list(map(int, input().split()))
        total_space += space

    total_block = B + sum(total_space)
    s_min, s_max = min(total_space), total_block // (M*N) 

    answer_time = 9999999999
    answer_height = 0

    for h in range(s_min, s_max+1):
        remain_b = B
        result = 0
        for now_h in total_space:
            if now_h > h:
                result, remain_b = extract(now_h, h, result, remain_b)
            elif now_h < h:
                result, remain_b = add(now_h, h, result, remain_b)
        if (result < answer_time) & (remain_b>=0):
            answer_time = result
            answer_height = h

    print(answer_time, answer_height)

        
