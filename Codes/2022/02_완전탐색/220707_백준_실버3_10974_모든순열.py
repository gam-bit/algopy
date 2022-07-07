# 브루트 포스, 백트레킹
# https://www.acmicpc.net/problem/10974


def recursive(n):
    global answer

    if len(answer) == n:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            recursive(n)
            answer.pop()

if __name__ == "__main__":
    n = int(input())
    answer = []
    recursive(n)