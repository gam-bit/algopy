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

# 주의!!! 
# dp
def makeone_dp(n):
    
    memo = [0] * (n+1)
    # memo의 index가 우리가 나눌 값
    # 1은 연산 횟수가 0이므로 따로 처리할 필요가 없음
    
    for i in range(2, n+1):
        lst = [] # 비교할 리스트

        if i % 5 == 0:
            find_idx = i//5
            lst.append(memo[find_idx] + 1)
        elif i % 3 == 0:
            find_idx = i//3
            lst.append(memo[find_idx] + 1)
        elif i % 2 == 0:
            find_idx = i//2
            lst.append(memo[find_idx] + 1)
        
        find_idx = i-1
        lst.append(memo[find_idx] + 1)
        
        memo[i] = min(lst)

    print(memo) 
    return memo[n]

    
x = int(input())

print(makeone_dp(x))


