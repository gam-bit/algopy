# 자료구조
# https://www.acmicpc.net/problem/4358
# 출력 부분에서 이슈가 생길 수 있음

from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(int)
cnt = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    cnt += 1

trees_lst = list(trees.keys())
tree_names = sorted(trees_lst)

for name in tree_names:
    # print(name, str(round(trees[name]/cnt*100, 4))) # 틀린 답
    print(name, "{:.4f}".format(trees[name]/cnt*100)) # 맞는 답

'''
python의 round함수 작동방식이 독특함. 
부동소수점 문제 해결을 위해 조절해놓은 부분이 있음
예) round(0.5) = 0 / round(1.5) = 2
'''

