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
 

def binarysearch_using_while(keep_lst, target):
    left = 0
    right = len(keep_lst) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if keep_lst[mid] == target:
            return 'yes'
        elif keep_lst[mid] > target:
            right = mid - 1
        elif keep_lst[mid] < target:
            left = mid + 1

    return 'no'


def binarysearch_using_recursive(keep_lst, target, l, r):    
    mid = (l+r)//2

    if l > r:
        return 'no'
    
    if keep_lst[mid] == target:
        return 'yes'

    elif keep_lst[mid] > target:
        return binarysearch_using_recursive(keep_lst, target, l, mid-1)
    
    else:
        return binarysearch_using_recursive(keep_lst, target, mid+1, r)




n = int(input())
keep_lst = list(map(int, input().split()))
keep_lst.sort()

m = int(input())
find_lst = list(map(int, input().split()))

while_answer = []
rec_answer = []
for t in find_lst:
    v1 = binarysearch_using_while(keep_lst, t)
    while_answer.append(v1)
    v2 = binarysearch_using_recursive(keep_lst, t, 0, len(keep_lst)-1)
    rec_answer.append(v2)

print('binarysearch_using_while: ')
print(' '.join(while_answer))
print('='*50)
print('binarysearch_using_recursive: ') 
print(' '.join(rec_answer))