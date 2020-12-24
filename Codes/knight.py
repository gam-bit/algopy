## <왕실의 나이트>
## 2020-12-24
## 난이도 1
## 풀이시간 20분
## 시간 제한 1초 | 메모리 제한 128MB
import itertools

board = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

# 주어진 자리 (x, y)
# 이동한 자리 (a, b)
x, y = list(input())
x = board[x]
y = int(y)

one = [1, -1]
two = [2, -2]

move = list(itertools.product(one, two)) + list(itertools.product(two, one))

cnt = 0

for i, j in move:
    a = x+i
    b = y+j
    if (a >= 1) & (a <= 8) & (b >= 1) & (b <= 8):
        cnt += 1
    # print(a, b, cnt)


print(cnt)
    

