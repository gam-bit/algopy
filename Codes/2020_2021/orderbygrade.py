## <성적이 낮은 순서로 학생 출력하기>
## 2020-12-28
## 난이도 1
## 풀이시간 20분
## 시간 제한 1초 | 메모리 제한 128MB
## 문제유형 : 정렬 

## <input>
##2
##홍길동 95
##이순신 77

## <output>
## 이순신 홍길동

#-------------------------------------------


def sort(students):
    
    n = len(students)
    
    for i in range(1, n):
        for j in range(i, 0, -1):
            
            if students[j][1] > students[j-1][1]:
                students[j-1], students[j] = students[j], students[j-1]

            else: 
                break
    
    return students


def quicksort(students):
    # 얼마나 정렬됐는지에 따라서 시간복잡도가 결정됨

    n = len(students)

    if n <= 1: # 재귀 탈출 조건
        return students
    
    pivot = students[n//2][1]  # 랜덤으로 알아서 설정하기
    
    less_lst = []
    equal_lst = []
    more_lst = []

    for n, s in students:
        if s < pivot:
            less_lst.append((n, s))
        elif s > pivot:
            more_lst.append((n, s))
        else:
            equal_lst.append((n, s))

    print(f"less: {less_lst}, equal: {equal_lst}, more: {more_lst}")
    return quicksort(less_lst) + equal_lst + quicksort(more_lst)



def countsort(students, k=101): # k : 숫자 범위(0점~100점)
    cnt_lst = [0] * k
    sort_lst = [0] * len(students)
     
    for i in students.values():
        cnt_lst[i] += 1

    for i in range(k-1): # 0 ~ 100
        cnt_lst[i+1] += cnt_lst[i]
    
    for n, s in students.items():
        sort_lst[cnt_lst[s]-1] = (n, s) 
        cnt_lst[s] -= 1

    return sort_lst




    


n = int(input())

# students = []
# for _ in range(n):
#     name, score = input().split()
#     students.append((name, int(score)))

# print(' '.join([n for n, s in quicksort(students)]))

students_dict = {}
for _ in range(n):
    name, score = input().split()
    students_dict[name] = int(score)

print("CountingSort :",' '.join([n for n, s in countsort(students_dict, 101)]))




