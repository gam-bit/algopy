# 자료구조 - 큐, 덱
# https://www.acmicpc.net/problem/5430


from collections import deque

t = int(input())

for _ in range(t):
    cmds = input()
    n = int(input())
    arr = input()[1:-1].split(',')

    if n == 0:
        queue = []
    else:
        arr = map(int, arr)
        queue = deque(arr)

    if n == 0:
        queue = []
    
    flag = 0
    try:
        for cmd in cmds:
            if cmd == "R":
                flag +=1 
            elif cmd == "D":
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

        if flag % 2 == 1:
            queue.reverse()
        print(str(list(queue)).replace(' ', ''))

    except:
        print('error')


"""
* 뒤집기를 매번 수행하지 X -> 뒤집기 짝수번이면 변화없음 -> flag 사용
* 뒤집기 상태에 따라 맨 앞수가 버려질 수도, 맨 뒷수가 버려질 수도 있음
  -> deque 사용 (pop, popleft)
* 결과는 str로 공백없이 출력
"""
    
            