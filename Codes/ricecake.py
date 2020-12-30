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
    

def search(h_lst, m, l, r, ch_lst):
    
    mid_idx = (l+r)//2
    dduck_len = sum_dduck_length(dduck_lst, h_lst[mid_idx])
    # print(h_lst[mid_idx], dduck_len)
    if l > r:
        return ch_lst
    
    if dduck_len == m:
        return [(h_lst[mid_idx], dduck_len)]

    elif dduck_len > m:
        ch_lst.append((h_lst[mid_idx], dduck_len))
        return search(h_lst, m, mid_idx+1, r, ch_lst)
    elif dduck_len < m:
        ch_lst.append((h_lst[mid_idx], dduck_len))
        return search(h_lst, m, l, mid_idx-1, ch_lst)
        
    

n, m = map(int, input().split())

dduck_lst = list(map(int, input().split()))

# h = 0 ~ 제일 긴 떡길이
longest = max(dduck_lst)
h_lst = [i for i in range(longest+1)] 

ch_lst = search(h_lst, m, 0, len(h_lst)-1, [])

print(ch_lst)
print(max([i[0] for i in ch_lst if i[1] >= m]))
    