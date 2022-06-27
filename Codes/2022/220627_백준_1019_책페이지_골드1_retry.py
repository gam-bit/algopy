# 자료구조 - 해시
# https://www.acmicpc.net/problem/1019

n = int(input())

answer_list = [0] * 10

for i in range(1, n+1):
    for letter in str(i):
        answer_list[int(letter)] += 1

answer_list = map(str, answer_list)
print(' '.join(answer_list))