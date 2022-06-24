def check_make(v, coins): 
    """
    > input : 만들고 싶은 값과 가지고 있는 화폐(sort된 상태)
    > output : 가능 여부 1 or 0
    """
    val = 0 # 코인들 합하면서 만들어지는 값. v하고 비교. 

    for i in coins: # [9, 3, 2, 1, 1] v = 3
        if i <= v-val: # v-val : 필요한 금액
            val += i

    if val == v:
        return 1
    return 0
            
        
if __name__ == '__main__':


    n = int(input()) # 동전 개수
    coins = list(map(int, input().split()))

    coins.sort(reverse=True)
    max_val = sum(coins)
    for i in range(1, max_val+2): # 1~17
        if check_make(i, coins) == 0: 
            print(i)
            break 
        
    
    