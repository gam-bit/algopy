## <떡볶이 떡 만들기>
## 2020-12-30
## 난이도 2
## 풀이시간 40분
## 시간 제한 2초 | 메모리 제한 128MB
## 문제 유형 : 이진 탐색

## <input>
# 4 6
# 19 15 10 17

## <Output>
# 15

#---------------------------------


# 잘라준 떡 길이의 총합
def sum_dduck_length(dduck_lst, h):
    return sum([dduck-h if dduck-h >= 0 else 0 for dduck in dduck_lst])  # [19, 15, 10, 17]
    

def search_while(dduck_lst, m):
    
    start = 0
    end = max(dduck_lst)
    
    while start <= end:
        mid = (start+end) // 2
        length = sum_dduck_length(dduck_lst, mid)
        
        if mid > length: # 떡이 더 필요
            end = mid - 1
        else: 
            result = mid # 떡이 정해놓은 길이보다 큰 경우는 성립함
            start = mid + 1
        
    

n, m = map(int, input().split())

dduck_lst = list(map(int, input().split()))

# h = 0 ~ 제일 긴 떡길이
longest = max(dduck_lst)
h_lst = [i for i in range(longest+1)] 

ch_lst = search(h_lst, m, 0, len(h_lst)-1, [])

print(ch_lst)
print(max([i[0] for i in ch_lst if i[1] >= m]))
    