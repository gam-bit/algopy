# https://www.acmicpc.net/problem/15649

def recursive(n, m):

    global str_num

    if len(str_num) == m:
        print(' '.join(list(str_num)))
        return 
    
    for i in range(1, n+1):
        str_i = str(i)
        if str_i not in str_num:
            str_num += str_i
            # print(f"after adding: {str_num}")
            recursive(n, m)
            str_num = str_num[:-1]
            # print(f"after extracting: {str_num}")


if __name__ == "__main__":
    n, m = map(int, input().split())
    str_num = ''
    recursive(n, m)
    