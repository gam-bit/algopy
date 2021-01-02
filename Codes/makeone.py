## <미로 찾기>
## 2021-01-02
## 난이도 1.5
## 풀이시간 20분
## 시간 제한 1초 | 메모리 제한 128MB
## 내용 : DP(동적계획법)

## <input>
# 26
## <output>
# 3
#--------------------------------------------------

# 재귀
def makeone(n, cnt = 0):
    
    if n == 1:
        return cnt

    if n % 5 == 0:
        return makeone(n//5, cnt+1)
    
    elif n % 3 == 0:
        return makeone(n//3, cnt+1)
    
    elif n % 2 == 0:
        return makeone(n//2, cnt+1)

    return makeone(n-1, cnt+1)


# 2) dp
def makeone_dp(n):
    
    memo = {}
    memo[1], memo[2], memo[3], memo[4], memo[5] = 1, 1, 1, 2, 1
    
    for i in range(6, n+1):
        if i % 5 == 0:
            memo[i] = memo[i//5] + 1
        elif i % 3 == 0:
            memo[i] = memo[i//3] + 1 
        elif i % 2 == 0:
            memo[i] = memo[i//2] + 1
        else:
            memo[i] = memo[i-1] + 1
    print(memo) 
    return memo[n]

    
x = int(input())

print(makeone(x))


