# https://www.acmicpc.net/problem/20057
"""
1. matrix transpose : list(zip(*list of list)) 사용 (이거 생각 못하면 실제로는 그냥 다 써서라도 하기)
"""

# 토네이도 시작점 => ((n-1)/2, (n-1)/2)

# 토네이도 이동
    # 방향 : 왼, 아래, 오, 위  => [(-1, 0), (0, -1), (1, 0), (0, 1)]
    # 크기 : 1, 1, 2, 2, 3, 3, 4, 4, ...

# 흩날리는 비율
    # [[0, 0, 0.02, 0, 0],
    #  [0, 0.1, 0.07, 0.01, 0],
    #  [0.05, 0, 0, 0, 0], # [0.05, 남은 모래, 도착, 출발, 0]
    #  [0, 0.1, 0.07, 0.01, 0],
    #  [0, 0, 0.02, 0, 0]]


def rotate90(proportion):
    new_p = list(zip(*proportion))[::-1]
    return new_p


n = 7
i, j = ((n-1)/2, (n-1)/2)

m = 0
m_value = 1
move_idx = [(-1, 0), (0, 1), (1, 0), (0, -1)]


print((i, j))
while True:
    if i <= 0 and j <= 0:
        raise ValueError

    k = m % 4 
    move_i, move_j = move_idx[k]

    i += move_i*m_value
    j += move_j*m_value
    
    

    m += 1
    if k == 1 or k == 3:
        m_value += 1

    print((i, j), m_value)