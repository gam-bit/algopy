# https://www.acmicpc.net/problem/15649

from itertools import permutations
from math import perm

n, m = map(int, input().split())

num_list = [i for i in range(1, n+1)]

final_list = list(permutations(num_list, m))
for t in final_list:
    print(' '.join([str(i) for i in t]))