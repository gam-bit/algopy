from collections import deque

n = int(input()) # test case 1~100
doc_list = []
queue_list = []

for _ in range(n):
    doc, m = map(int, input().split()) # 문서번호(1부터), 인쇄 queue위치(0부터)
    queue = deque(list(map(int, input().split()))) # 문서 중요도 리스트
    doc_list.append([doc, m])
    queue_list.append(queue)

for i in range(n):
    doc, m = doc_list[i]
    queue = queue_list[i]
    count = 0

    while queue:
        max_q = max(queue)
        q = queue.popleft()
        m += -1

        # 현재 q == max_q => 프린트
        if max_q == q:
            count += 1
            if m < 0:
                print(count)
                break

        # 현재 q < max_q => 뒤로 이동
        else:
            queue.append(q)
            if m < 0:
                m = len(queue)-1


