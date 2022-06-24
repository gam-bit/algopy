# 자료구조 - 스택
# https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

class Stack:
    
    def __init__(self):
        self.s_list = []

    def push(self, value):
        self.s_list.append(value)

    def size(self):
        return len(self.s_list)

    def empty(self):
        if self.size() == 0:
            return 1
        return 0

    def top(self):
        if not self.empty():
            return self.s_list[-1]
        return -1
    
    def pop(self):
        if not self.empty():
            return self.s_list.pop()
        return -1

def trace(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"time : {time.time() - start}sec")
        return result
    return wrapper

@trace
def main(k):
    stack = Stack()
    for _ in range(k):
        val = int(input())
        if val != 0:
            stack.push(val)
        else:
            stack.pop()
    return sum(stack.s_list)

if __name__ == "__main__":
    
    k = int(input())
    print(main(k))

