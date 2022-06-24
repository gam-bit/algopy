# 방법1) 수학
def count_cases_using_math(n, m, ball_lst):
    total_comb = n * (n-1)/2

    excepted_case = 0
    for i in range(1, m+1):
        same_balls = [ball for ball in ball_lst if ball==i] 
        n_same_balls = len(same_balls) 
        if n_same_balls >= 2:
            excepted_case += (n_same_balls) * (n_same_balls-1) / 2
        
    return int(total_comb - excepted_case)


# 방법2) 그리디
    ## 내림차순 정렬한 ball_lst의 index만큼 짝지을 수 있음
    ## 예) [3, 3, 2, 2, 1] 일 때, 
    ##     먼저 1로 짝지을 수 있는 경우의 수 = 4 = 1의 index
    ##          2로 짝지을 수 있는 경우의 수 = 2 = 2의 index(첫번째꺼 반환함)
    ##         3으로 짝지을 수 있는 경우의 수 = 0 = 3의 index
def count_cases(n, ball_lst):
    ball_lst.sort(reverse=True)
    
    cnt = 0
    for ball in ball_lst[::-1]:
        cnt += ball_lst.index(ball) 
 
    return cnt


if __name__ == '__main__':
    n, m = map(int, input().split())
    ball_lst = list(map(int, input().split()))
    print(f"수학 사용: {count_cases_using_math(n, m, ball_lst)}")
    print(f"그리디 사용: {count_cases(n, ball_lst)}")