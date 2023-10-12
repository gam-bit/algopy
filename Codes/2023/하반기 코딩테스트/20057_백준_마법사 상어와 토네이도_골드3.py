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

def main(n, graph):
    p = [[0, 0, 0.02, 0, 0],
         [0, 0.1, 0.07, 0.01, 0],
         [0.05, 0, 0, 0, 0], # [0.05, 남은 모래, 도착, 출발, 0]
         [0, 0.1, 0.07, 0.01, 0],
         [0, 0, 0.02, 0, 0]]

    x_i, x_j = (int((n-1)/2), int((n-1)/2)) # x : 현 위치 

    m = 0
    m_value = 1
    move_idx = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    alpha_idx = [(2, 1), (3, 2), (2, 3), (1, 2)]

    sand_out = 0
    
    while True:

        k = m % 4 
        move_i, move_j = move_idx[k]
        alpha_i, alpha_j = alpha_idx[k]

        # y의 모래 양 확인
        for _ in range(m_value):
            y_i = x_i + move_i
            y_j = x_j + move_j

            if y_i < 0 or y_j < 0 or y_i >= n or y_j >= n:
                return sand_out
            
            sand_y = graph[y_i][y_j]

            if sand_y == 0:
                x_i, x_j = y_i, y_j
                continue

            graph[y_i][y_j] = 0

            sand_move = [[int(i*sand_y) for i in l] for l in p]
            sand_move_total = sum([sum(i) for i in sand_move])
            alpha = sand_y - sand_move_total
            sand_move[alpha_i][alpha_j] = alpha

            # 모래 이동
                # 기준점 (2, 2) = y 위치
                # 범위 (0,0) ~ (4, 4)
            for a in range(-2, 3):
                for b in range(-2, 3):
                    sand = sand_move[2+a][2+b]
                    if sand:
                        check_i, check_j = y_i+a, y_j+b
                        if check_i >= 0 and check_i < n and check_j >=0 and check_j < n:
                            graph[check_i][check_j] += sand
                        else:
                            sand_out += sand

            x_i, x_j = y_i, y_j

        p = rotate90(p)
    
        m += 1
        if k == 1 or k == 3:
            m_value += 1


if __name__=="__main__":
    n = int(input())
    graph = [[int(i) for i in input().split(' ')] for _ in range(n)]

    print(main(n, graph))