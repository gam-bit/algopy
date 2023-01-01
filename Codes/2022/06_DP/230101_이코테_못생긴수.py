# 교재는 최소공배수를 하나씩 넣어주는 방법 사용 -> 인덱스 2개 활용(memoization idx, 배수구하는 idx)
# 나는 숫자를 인수분해하는 방법 사용
memo = [1, 1] + [0] * 1000

def get_ugly_num(n):
    if memo[n] != 0:
        return n

    idx = memo.index(0)
    last_ugly_num = memo[idx-1]
    ugly_num = last_ugly_num + 1

    while not memo[n]:
        temp_num = ugly_num
        for i in [2, 3, 5]:   
            if temp_num == 1:
                break
            while temp_num % i == 0:
                temp_num //= i
        if temp_num == 1:
            memo[idx] = ugly_num
            idx += 1
            ugly_num += 1
        else:
            ugly_num += 1 
    return memo[n]
            
    
if __name__=="__main__":
    n = int(input())
    print(get_ugly_num(n))
    print(memo[:n+2])
