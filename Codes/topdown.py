## <위에서 아래로>
## 2020-12-28
## 난이도 1
## 풀이시간 15분
## 시간 제한 1초 | 메모리 제한 128MB
## 문제유형 : (내림차순) 정렬

## <input>
##3
##15
##27
##12
## <output>
## 27 15 12

#------------------------------------------


# 버블 정렬
def sort(numbers):
    n = len(numbers)
    swap = 0 ## 이거 맨날 까먹음!!!

    for i in range(n)[::-1]:  # n-1, n-2개씩 array를 확인
        for j in range(i):  
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swap += 1
        
        if swap == 0:
            break

    return numbers



n = int(input())
seq = []
for _ in range(n):
    seq.append(int(input()))

print(' '.join(map(str, sort(seq))))
                
        
            



