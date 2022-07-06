# https://www.acmicpc.net/problem/15650

def recursive(n, m):
    global str_num

    if len(str_num) == m+1:
        print(' '.join(list(str_num[1:])))
        return
    
    for i in range(1, n+1):
        str_i = str(i)
        if i > int(str_num[-1]):
            str_num += str_i
            recursive(n, m)
            str_num = str_num[:-1]


if __name__ == "__main__":
    n, m = map(int, input().split())
    str_num = "0"
    recursive(n, m)
