# https://programmers.co.kr/learn/courses/30/lessons/43165

from itertools import combinations


def solution(numbers, target):
    
    answers = []
    idx_lst = [i for i in range(len(numbers))]
    for i in range(1, len(numbers)+1):
        comb = combinations(idx_lst, i)

        for c in comb:
            values = [-num if idx in c else num for idx, num in enumerate(numbers)]
            answer = sum(values)
            answers.append(answer)

    return answers.count(target)



print(solution([1,1,1,1, 1], 3)) # 5


#--------------------------------
# very 아름다운 코드
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    # print(list(product(*l)))
    return s.count(target)