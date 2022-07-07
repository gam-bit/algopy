# 수학 -> retry
# https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

def method_using_math(n, m):
    if n < m:
        return 0
    elif m == 0:
        return 10 ** n
    else:
        return m * method_using_math(n-1, m-1) + (10-m) * method_using_math(n-1, m)

if __name__ == "__main__":
    n, m = map(int, input().split())

    if m > 0:
        num_list = list(map(int, input().split()))
    else:
        num_list = []
    print(method_using_math(n, m))
