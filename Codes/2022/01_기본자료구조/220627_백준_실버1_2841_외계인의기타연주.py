# 자료구조 - 스택
# https://www.acmicpc.net/problem/2841
import sys
input = sys.stdin.readline

n, p = map(int, input().split())

stacks = [[] for _ in range(6)]

cnt = 0
for i in range(n):
    j, q = map(int, input().split())
    
    stack = stacks[j-1]
    if not stack:
        stack.append(q)
        cnt += 1
    else:
        top_val = stack[-1]
        while top_val != q:    
            if top_val > q:
                stack.pop()
                cnt += 1
            else:
                stack.append(q)
                cnt += 1
            top_val = stack[-1] if stack else 0
    stacks[j-1] = stack

print(cnt)


