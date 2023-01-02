# 2022 카카오 테크 인턴십 기출

# https://school.programmers.co.kr/learn/courses/30/lessons/118667
# [3,2,7,2], [4,6,5,1] => 7
"""
1. 최대 이동 횟수는 수학적으로 접근해야하는데 정확하게 알기가 어려움. 이런 때엔 숫자를 키워가면서 테스트 해봐야 함.
2. sum을 매번 구하는 시간 > sum을 처음에 한 번만 구하고 더하기 빼기로 변경시키는 시간
"""

from collections import deque

def solution(a_q, b_q):
    a_q = deque(a_q)
    b_q = deque(b_q)
    
    sum_a = sum(a_q)
    sum_b = sum(b_q)
    
    if (sum_a + sum_b) % 2 == 1:
        return -1
    
    cnt = 0
    limit = 4*len(a_q)

    while True:
        # 종료 조건
        if sum_a == sum_b:
            return cnt    

        if (not a_q) | (not b_q):
            return -1
        
        if limit <= cnt:
            return -1
        
        # 종료 아닐 때
        if a_q and (sum_a > sum_b):
            m = a_q.popleft()
            b_q.append(m)
            sum_a -= m
            sum_b += m
        
        elif b_q and (sum_a < sum_b):
            m = b_q.popleft()
            a_q.append(m)
            sum_a += m
            sum_b -= m
            
        cnt += 1
        


    
if __name__=="__main__":
    x_list = deque([3,2,7,2])
    y_list = deque([4,6,5,1])
    print(solution(x_list, y_list))

