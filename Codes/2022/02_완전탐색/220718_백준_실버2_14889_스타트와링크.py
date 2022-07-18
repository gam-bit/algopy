# https://www.acmicpc.net/problem/14889
import itertools

def calculate_ab(comb, ab_list):
    new_combs = itertools.combinations(comb, 2)
    total_ab = 0
    for new_comb in new_combs:
        i, j = new_comb
        total_ab += ab_list[i][j]
        total_ab += ab_list[j][i]
    return total_ab


if __name__ == "__main__":

    n = int(input())

    ab_list = []
    for _ in range(n):
        one_list = list(map(int, input().split()))
        ab_list.append(one_list)

    combs = list(itertools.combinations([i for i in range(n)], int(n/2)))
    num_combs = len(combs)

    min_diff = 100
    while (len(combs) != 0) & (min_diff != 0):
        comb = combs.pop()
        other_comb = tuple([i for i in range(n) if i not in comb])
        combs.remove(other_comb)
        
        ab_comb = calculate_ab(comb, ab_list)
        ab_other_comb = calculate_ab(other_comb, ab_list)

        diff = abs(ab_comb-ab_other_comb)
        min_diff = min(min_diff, diff)

    print(min_diff)
        