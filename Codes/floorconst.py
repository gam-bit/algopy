## <바닥 공사>
## 2021-01-03
## 난이도 1.5
## 풀이시간 20분
## 시간 제한 1초 | 메모리 제한 128MB
## 내용 : DP(동적계획법)

## <input>
# 3
## <output>
# 5

#------------------------
from itertools import permutations

# 배열 개수
def cnt_perm(lst): 
    return len(set(permutations(lst, len(lst))))



# 숫자들을 1, 2의 조합으로 나타내기
def johap(n):
    memo = [[]] * (n+1)

    memo[1] = [[1]]
    memo[2] = [[1, 1], [2]]

    
    for i in range(3, n+1):
        johap_lst = [j+[1] for j in memo[i-1]]
        if i % 2 == 1:
            memo[i] = johap_lst
        else:
            lstby2 = [[2] * (i//2)] 
            memo[i] = johap_lst + lstby2
    
    print(memo)
    return memo[n]



def solution(n):
    cnt = 0
    
    for lst in johap(n):
        v = 1
        for i in lst:
            v *= i
        v *= cnt_perm(lst)
        cnt += v
    
    return cnt

#---------------------------------------------
# 점화식 만들기 

def answer_dp(n):
    memo = [0] * 1001
    
    memo[1] = 1
    memo[2] = 3
    
    for i in range(3, n+1):
        memo[i] = 2 * memo[i-2] + memo[i-1]

    return memo[n]

n = int(input())
print(answer_dp(n))

