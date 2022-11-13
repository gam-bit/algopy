# 비교하는 부분 없이 작성하는 것이 좋음(메모리 사용 줄이기)

def dfs_mj(numbers, cumsum=0):
    cumsum_list = []
    if not numbers:
        return cumsum
    else:
        num = numbers[0]
        cumsum_plus = dfs(numbers[1:], cumsum=cumsum + num)
        cumsum_minus = dfs(numbers[1:], cumsum=cumsum - num)
        if isinstance(cumsum_plus, list):
            cumsum_list += cumsum_plus
        else:
            cumsum_list.append(cumsum_plus)
        if isinstance(cumsum_minus, list):
            cumsum_list += cumsum_minus
        else:
            cumsum_list.append(cumsum_minus)
    return cumsum_list
        
def solution_mj(numbers, target):
    result = dfs_mj(numbers)
    return sum([1 for i in result if i == target])

#------------------------------------------------#
#                     정답                       #
#------------------------------------------------#
def dfs(numbers, target, cumsum):
    answer = 0
    if not numbers and target == cumsum:
        return 1
    elif not numbers:
        return 0

    answer += dfs(numbers[1:], target, cumsum+numbers[0])
    answer += dfs(numbers[1:], target, cumsum-numbers[0])
    return answer

def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer


if __name__=="__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3 
    print(solution(numbers, target)) # 5

    