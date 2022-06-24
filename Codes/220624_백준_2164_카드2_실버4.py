# 자료구조 - 큐
# https://www.acmicpc.net/problem/2164

from collections import deque

class Queue:
    
    def __init__(self, n):
        self.q_list = deque([i for i in range(1, n+1)])

    def enqueue(self, k):
        self.q_list.append(k)

    def size(self):
        return len(self.q_list)
    
    def dequeue(self):
        if not self.empty():
            return self.q_list.popleft()
        return -1

    def empty(self):
        if self.size() > 0:
            return 0
        return 1
    
    def front(self):
        if not self.empty:
            return self.q_list[0]
        return -1

    def back(self):
        if not self.empty:
            return self.q_list[-1]
        return -1 


if __name__ == "__main__":
    import time
    start = time.time()
    card_num = int(input())
    q = Queue(card_num)

    while q.size() != 1:
        q.dequeue()
        pop_card = q.dequeue()
        q.enqueue(pop_card)
    print(q.q_list[0])
    print("time :", time.time() - start)