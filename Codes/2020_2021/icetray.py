## <음료수 얼려 먹기>
## 2020-12-26
## 난이도 1.5
## 풀이시간 20분
## 시간 제한 1초 | 메모리 제한 128MB


n, m = map(int, input().split())
tray = []
for i in range(n):
    tray.append(list(map(int, input())))



def solution(tray, i, j):
    if (i >= n) | (j >= m) | (i < 0) | (j < 0):
        return 0
    elif tray[i][j] == 0:
        tray[i][j] = 1
        solution(tray, i, j+1)  # 오른쪽
        solution(tray, i+1, j)  # 아래
        solution(tray, i, j-1) # 왼쪽
        return 1 
    return 0


cnt = 0
for a in range(n):
    for b in range(m):
        cnt += solution(tray, a, b)

print(cnt)



