# https://www.acmicpc.net/problem/2239

import sys
input = sys.stdin.readline

def calculate(board, i, j, num):
    # 가로
    if num in board[i]:
        return False
    # 세로
    col = [row[j] for row in board]
    if num in col:
        return False

    # 정사각형
    row_idx = i//3 * 3
    col_idx = j//3 * 3
    row_idx_list = [row_idx, row_idx+1, row_idx+2]
    col_idx_list = [col_idx, col_idx+1, col_idx+2]

    square = [board[r][c] for r in row_idx_list for c in col_idx_list]
    if num in square:
        return False

    return True


def solution(board, zeros):
    if not zeros:
        return board
    else:
        i, j = zeros[0]
        for num in range(1, 10):
            if calculate(board, i, j, num):
                board[i][j] = num
                result = solution(board, zeros[1:])
                if result:
                    return result
                board[i][j] = 0
        # 주어진 board에서 solution이 존재하지 않는 경우
        return []                    
    


if __name__ == "__main__":
    board = [list(map(int, list(input().strip()))) for _ in range(9)]
    zeros = [(i, j) for i in range(9) for j in range(9) if not board[i][j]]
    answer = solution(board, zeros)

    for line in answer:
        print(''.join(list(map(str, line))))


"""
문제 풀이 key point
1) 스도쿠 구현
    - 정사각형 살펴보기
2) 재귀 + 백트래킹
"""