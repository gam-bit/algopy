# https://www.acmicpc.net/problem/1300
# 답) https://claude-u.tistory.com/449

# n * n 숫자들에서 m이하인 숫자가 몇 개 인지 구할 수 있음
# m이하인 숫자가 k개인지를 확인 
# 적절한 m을 찾는 문제




def cnt_numbers(n, m):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(m//i, n)
    return cnt

def solution(n, k):
    
    start = 0
    end = n**2-1

    while start < end:
        mid = (start+end)//2
        cnt = cnt_numbers(n, mid)
        print(mid, cnt)
        if cnt >= k:
            answer = mid # ★★★★★★★★
            end = mid-1
        elif cnt < k:
            start = mid+1

    return answer        

        

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(solution(n, k))