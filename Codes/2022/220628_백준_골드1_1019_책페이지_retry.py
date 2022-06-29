# https://www.acmicpc.net/problem/1019

# 숫자 세는 방법
    ## 10의 거듭제곱으로 숫자를 나눈 몫을 가져옴 -> n
        ## 만약 n = 0 -> 10의 거듭제곱이 주어진 숫자의 제일 높은 자리수에 해당하는 자리임 
            ## 해당 자리에 온 숫자 확인해서 = k
                ## 0보다크고 k보다 작은 수 : 나눈 10의 거듭제곱보다 지수 하나 작은 거듭제곱만큼 더하기
                ## k : 10의 거듭제곱으로 숫자를 나눈 나머지 + 1만큼 더하기
        ## n != 0
            ## 0 : n-1 / 1~9 : n
            ## 10의 거듭제곱으로 숫자를 나눈 나머지 = v
                ## 0 이상 k 미만인 수 : 주어진 10의 거듭제곱 보다 지수 하나 작은 거듭제곱 만큼 더해줌
                    ### 10 ** (처음에 나눈 값 - 1)
                ## k : v + 1

def add_first_digit(answer_list, num):
    digit = len(str(num))
    divider = 10**(digit-1)
    top_value, remainder = num // divider, num % divider

    for i in range(10):
        if 0 < i < top_value:
            answer_list[i] += divider
        elif i == top_value:
            answer_list[i] += (remainder + 1)
    return answer_list
    

def add_digit_except_first(answer_list, num, digit):
    divider = 10 ** digit
    divider_digit = 10 ** (digit-1)
    quotient, remainder = num // divider, num % divider
    k, v = remainder // divider_digit, remainder % divider_digit

    for i in range(10):
        if i == 0:
            answer_list[0] += divider_digit * (quotient-1)
        else:
            answer_list[i] += divider_digit * quotient

        if i < k:
            answer_list[i] += divider_digit
        elif i == k:
            answer_list[i] += v + 1
    
    return answer_list
    

if __name__ == "__main__": 
    n = int(input())

    answer_list = [0] * 10
    digit = len(str(n))

    for i in range(1, digit):
        answer_list = add_digit_except_first(answer_list, n, i)
    answer_list = add_first_digit(answer_list, n)

    print(' '.join([str(i) for i in answer_list]))