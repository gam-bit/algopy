# 백트래킹 -> python3 시간초과, pypy3 OK
# https://www.acmicpc.net/problem/9663
import sys
from turtle import back
input = sys.stdin.readline

def backtracking(n, m, num_list):
    total_cnt = 0
    for i in range(10**n):
        str_num = str(i).zfill(n)
        flag = 0
        if all(map(lambda i: str(i) in str_num, num_list)):
            total_cnt += 1
    return total_cnt

if __name__ == "__main__":
    n, m = map(int, input().split())

    if m > 0:
        num_list = list(map(int, input().split()))
    else:
        num_list = []
    print(backtracking(n, m, num_list))
