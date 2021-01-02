# https://www.fun-coding.org/Chapter14-dp_divide.html

# 1) 재귀

def fibo_rec(num):
    if num == 0:
        return 0

    elif num < 3:
        return 1

    return fibo_rec(num - 1) + fibo_rec(num - 2)

print(fibo_rec(10))


# 2) DP
# - recursion이 불필요하게 잡아먹는 function call을 없애기 위해 기록을 남김
# - recursion에서 overlapping sub-instance가 많은 경우 사용

def fibo_dp(num):
    dictFibo = {}
    dictFibo[0] = 0
    dictFibo[1] = 1
    
    for i in range(2, num+1):
        dictFibo[i] = dictFibo[i-1] + dictFibo[i-2]
    return dictFibo[num]

print(fibo_dp(10))