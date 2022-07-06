# brute force -> 시간초과
# https://www.acmicpc.net/problem/18111

from collections import Counter
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

total_space = []
for _ in range(N):
    space = list(map(int, input().split()))
    total_space += space

total_B = sum(total_space) + B
h_min, h_max = min(total_space), total_B // (N*M)

answer_time = 10000000000
answer_height = 0
heights = Counter(total_space)
for i in range(h_min, h_max+1):
    time = 0
    for h, cnt in heights.items():
        if cnt > 0:
            if h > i:
                time += 2 * abs(h-i) * cnt
            elif h < i:
                time += abs(h-i) * cnt
    if time <= answer_time:
        answer_time = time
        answer_height = i

print(answer_time, answer_height)
        


"""
* 시간초과 해결방법 *
- 블럭을 쌓을 수 있는 최소~최대 높이 정하기 -> 최대 : 블럭 개수 세서 지정
- space를 하나씩 불러오지 않고 Counter를 써서 같은 높이의 space는 한 번에 계산
"""