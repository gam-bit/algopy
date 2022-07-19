# https://www.acmicpc.net/problem/14888
import itertools
import sys
input = sys.stdin.readline

n = int(input())
num_seq = list(map(int, input().split()))
oper_num_seq = list(map(int, input().split())) # 순서) + - x /
opers = ['+', '-', 'x', '/']
oper_seq = []
for i, j in zip(opers, oper_num_seq):
    oper_seq += [i] * j 

oper_perms = list(set(itertools.permutations(oper_seq)))
max_val = -1000000000
min_val = 1000000000
for opers in oper_perms:
    fst_num = num_seq[0]
    for scd_num, oper in zip(num_seq[1:], opers):
        if oper == '+':
            fst_num += scd_num
        elif oper == '-':
            fst_num -= scd_num
        elif oper == 'x':
            fst_num *= scd_num
        elif oper == '/':
            q = abs(fst_num) // abs(scd_num)
            if fst_num * scd_num < 0:
                fst_num = -q
            else:
                fst_num = q
    
    max_val = max(max_val, fst_num)
    min_val = min(min_val, fst_num)

print(max_val)
print(min_val)