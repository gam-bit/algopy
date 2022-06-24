## <두 배열의 원소 교체>
## 2020-12-29
## 난이도 1
## 풀이시간 20분
## 시간 제한 2초 | 메모리 제한 128MB
## 문제유형 : 정렬 

## <input>
##5 3
##1 2 5 4 3
##5 5 6 6 5

## <output>
## 26

#-------------------------------------------
n, k = map(int, input().split())

a_lst = list(map(int, input().split())) # 오름차순 정렬 [1, 6, 6, 6, 6]
b_lst = list(map(int, input().split())) # 내림차순 정렬 [6, 6, 5, 5, 5]


# 1) sort함수 만들어서 a_lst, b_lst 정렬하기
# 2) 원소 바꾸기

def quicksort(lst):
    
    n = len(lst)

    if n <= 1:
        return lst

    pivot = lst[0]

    less_lst, equal_lst, more_lst = [], [], []
    
    for v in lst:
        if v > pivot:
            more_lst.append(v)
        elif v < pivot:
            less_lst.append(v)
        else:
            equal_lst.append(v)

    return quicksort(less_lst) + equal_lst + quicksort(more_lst) # 오름차순


print('바꾸기 전 배열 A와 합:', a_lst, '->', sum(a_lst))
a_lst = quicksort(a_lst)
b_lst = quicksort(b_lst)[::-1]

for i in range(k):
    if a_lst[i] <= b_lst[i]:
        a_lst[i], b_lst[i] = b_lst[i], a_lst[i]
    else:
        break
print('바꾸기 후 배열 A와 합:', a_lst,'->', sum(a_lst))




