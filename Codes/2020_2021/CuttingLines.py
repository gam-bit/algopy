# https://www.acmicpc.net/problem/1654
# 문제 유형 : 이진 탐색

# <input>
# 4 11
# 802
# 743
# 457
# 539
# <output>
# 200

#------------------------------------------



# k <= n 이므로 
# 제일 길게 랜선을 자르는 경우는 
# 제일 짧은 랜선의 길이로 맞추는 것
# 랜선 길이 = 1 ~ 랜선 길이 최솟값 -> 해당 범위를 이진 탐색



def count_line_parts(lines_lst, h):
    return sum([i//h for i in lines_lst])
    
    
# k: 가지고 있는 랜선 수, n: 필요한 랜선 수
k, n = map(int, input().split()) 

lines = []
for _ in range(k):
    lines.append(int(input()))

# 반복문 사용

# answer_lst = []
start = 1
end = min(lines)

while start <= end:
    mid = (start + end) // 2
    cnt_parts = count_line_parts(lines, mid)

    if n < cnt_parts:
        end = mid - 1
    else:
        answer = mid
        # answer_lst.append((answer, cnt_parts))
        start = mid + 1
    

print(mid)