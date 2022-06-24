# https://programmers.co.kr/skill_checks/239483?challenge_id=2577
# test case 2개 시간초과

"""
number	    k | return
1924	    2 | 94
1231234	    3 | 3234
4177252841	4 | 775841
"""

def solution(number, k):
    
    answer = ''
    right_len = len(number) - k
    
    while len(answer) != right_len:
        # 맨 앞자리 수를 제일 크게 만들어 놓기
            ## 앞자리 수 max_idx개 제거
        max_idx = 0
        max_val = 0
        for i in range(k+1):
            if max_val < int(number[i]):
                max_val = int(number[i])
                max_idx = i
        
        answer += number[max_idx]
        number = number[max_idx+1:]
        k -= max_idx
            

    return answer

print(solution('1924', 2))