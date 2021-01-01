# https://www.acmicpc.net/problem/1654
#------------------------------------------



# k <= n 이므로 
# 제일 길게 랜선을 자르는 경우는 
# 제일 짧은 랜선의 길이로 맞추는 것
# 랜선 길이 = 1 ~ 랜선 길이 최솟값 -> 해당 범위를 이진 탐색

## step1) 주어진 범위를 이진 탐색하면서 랜선 길이 length 정하기
        ## 재귀 탈출 조건
            ## l > r
                ## 랜선 개수를 1개씩 늘려서 탐색
        ## length에 따른 랜선 개수(=m)를 구함
        ## -> m != n : 저장된 정보에 m==n인 상황이 있는지 확인. 있으면 해당 해당 length을 return
            ## -> m > n : (length, m) 저장하고 -> length 더 큰 수로
            ## -> m < n : (length, m) 저장하고 -> length 더 작은 수로
            ## -> m == n -> step2
                ## step2) m == n 
                        ## (length, m)만 저장하고 -> length:=length+1



def search(lines_lst, length_lst, n, l, r, info_lst): 
    print(info_lst)


    # 탈출 조건1
        ## 랜선 n개가 나오지 않은 경우이므로 
        ## 랜선 n+1개가 되는 상황을 찾기
    if l > r:
        return search(lines_lst, length_lst, n+1, 0, len(length_lst)-1, [])
    

    mid_idx = (l+r)//2
    h = length_lst[mid_idx]
    cnt_parts = count_line_parts(lines_lst, h) # h로 잘랐을 때, 랜선 수

    # 탈출 조건2
    if len(info_lst) != 0:
        if (len(info_lst) == 1) & (info_lst[0][1] == n):
            print('★★★★★', info_lst)
            return info_lst


    if n > cnt_parts:
        info_lst.append((h, cnt_parts))
        return search(lines_lst, length_lst, n, l, mid_idx, info_lst)

    elif n < cnt_parts:
        info_lst.append((h, cnt_parts))
        return search(lines_lst, length_lst, n, mid_idx+1, r, info_lst)

    elif n == cnt_parts:
        info_lst = [(h, cnt_parts)]
        while h > min(lines_lst):
            h += 1
            cnt_parts = count_line_parts(lines_lst, h)
            if n == cnt_parts:
                info_lst = [(h, cnt_parts)]
            else:
                return search(lines_lst, length_lst, n, 0, len(length_lst)-1, info_lst)

                
        


        
def count_line_parts(lines_lst, h):
    return sum([i//h for i in lines_lst])
    
    


# k: 가지고 있는 랜선 수, n: 필요한 랜선 수
k, n = map(int, input().split()) 

lines = []
for _ in range(k):
    lines.append(int(input()))

length_lst = [i for i in range(1, min(lines)+1)]

print(search(lines, length_lst, n, 0, min(lines)+1, []))