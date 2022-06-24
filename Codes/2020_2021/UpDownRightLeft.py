
## <상하좌우>
## 2020-12-24
## 난이도 1
## 풀이시간 15분
## 시간 제한 1초 | 메모리 제한 128MB


n = int(input())
plan = list(input().split())

x, y = 1, 1 # 각 숫자는 1이상 n이하

for i in plan:
    if i == 'R':
        if (y + 1 <= n):
            y += 1
    elif i == 'L':
        if (y - 1 >= 1):
            y -= 1
    elif i == 'D':
        if (x + 1 <= n):
            x += 1
    else:
        if (x - 1 >= 1):
            x -= 1
    # print(x, y)

print(x, y)


