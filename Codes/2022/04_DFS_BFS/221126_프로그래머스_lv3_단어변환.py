# https://school.programmers.co.kr/learn/courses/30/lessons/43163#

from collections import deque

def is_one_alpha_diff(word, new_word):

    if sum([i==j for i, j in zip(word, new_word)]) == len(word)-1:
        return True
    return False
    

def solution(begin, target, words):

    if target not in words:
        return 0
    
    check = [True] * len(words)
    q = deque()
    q.append((begin, 0))
    
    while q:
        word, dist = q.popleft()

        if word == target:
            return dist
        
        for i, new_word in enumerate(words):
            if is_one_alpha_diff(word, new_word) and check[i]:
                q.append((new_word, dist+1))
                check[i] = False
    return 0

if __name__=="__main__":
    begin = 'hit'
    target = 'cog'
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))

