memoization = [1, 1] + [0] * 100000
def top_down(num):
    if memoization[num] != 0:
        return memoization[num]
    print(f"들어간 숫자: {num}") # 재귀호출을 메모리에 쌓을 때 작동
    memoization[num] = top_down(num-1) + top_down(num-2)
    print(f"f_{num}번째 함수값 저장") # 모든 재귀호출이 메모리에 쌓인 후에 작동
    return memoization[num]
    


def bottom_up(num):
    memo = [0] * 1000000
    memo = [1, 1] + memo
    if num == 0 or num==1:
        return memo[num]
    
    for i in range(2, num+1):
        memo[i] = memo[i-1] + memo[i-2]
    
    return memo[num]


def recursive(num):
    if num == 0 or num ==1:
        return 1
    print(f"들어간 숫자: {num}") # 재귀호출을 메모리에 쌓을 때 작동
    result = recursive(num-1) + recursive(num-2)
    print(f"f_{num}번째 함수값 저장") # 모든 재귀호출이 메모리에 쌓인 후에 작동
    return result
    

if __name__=="__main__":
    num = input("몇번째 피보나치 수? ")
    print(top_down(int(num)))
    