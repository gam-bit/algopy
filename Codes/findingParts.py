## <부품 찾기>
## 2020-12-30
## 난이도 1.5
## 풀이시간 30분
## 시간 제한 1초 | 메모리 제한 128MB
## 문제 유형 : 이진 탐색

## <input>
# 5
# 8 3 7 9 2
# 3
# 5 7 9

## <output>
# no yes yes

#-----------------------------------------
# >> 이건 timeout

# n = int(input())
# keep_lst = list(map(int, input().split()))

# m = int(input())
# find_lst = list(map(int, input().split()))

# answer = []
# for i in find_lst:
#     if i in keep_lst:
#         answer.append('yes')
#     else:
#         answer.append('no')

# print(' '.join(answer))

#-------------------------------
# 이진 탐색으로 timeout 해결하기 -- O(logN)
# 이진 탐색은 정렬된 상태에서 시작
 

def search(lst, target):

    start_idx = 0
    mid_idx = len(lst)//2
    end_idx = len(lst)-1

    if end_idx == -1: # 빈 리스트
        return 'no'
    if (mid_idx == end_idx) & (lst[mid_idx] < target): # 제일 큰 수를 봤는데 target이 더 큰 경우
        return 'no'   
    
    if target == lst[mid_idx]:
        return 'yes'
    elif target > lst[mid_idx]:
        return search(lst[mid_idx+1:], target)
    else:
        return search(lst[:mid_idx], target)
    


n = int(input())
keep_lst = list(map(int, input().split()))
keep_lst.sort()

m = int(input())
find_lst = list(map(int, input().split()))

answer = []
for t in find_lst:
    v = search(keep_lst, t)
    answer.append(v)
    print(answer)

print(' '.join(answer))