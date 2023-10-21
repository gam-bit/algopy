# https://school.programmers.co.kr/learn/courses/30/lessons/214288

from itertools import combinations_with_replacement, permutations
import heapq

def calc_waiting_time(a, hq):
    """
    :param a: 특정 상담 유형의 멘토 수
    """
    wating_time = 0
    rooms = [0 for _ in range(a)] # 최대 a개 원소
    
    for req in hq:
        start, duration, _ = req
        prev_end = heapq.heappop(rooms)
        if start >= prev_end:
            heapq.heappush(rooms, start+duration)
        else:
            wating_time += prev_end - start
            heapq.heappush(rooms, prev_end+duration)
    return wating_time
                
def get_all_mentor_combs(k, n):
    combs = [v for v in list(combinations_with_replacement([i for i in range(1, n+1)], k)) if sum(v) == n]
    all_combs = []
    for c in combs:
        all_combs += list(set(permutations(c)))
    return all_combs

def solution(k, n, reqs):
    all_combs = get_all_mentor_combs(k, n)
    
    min_result = 1e10
    for c in all_combs:
        mentors_cnt = {i: c[i-1] for i in range(1, k+1)}
        answer = sum([calc_waiting_time(mentors_cnt[i], [r for r in reqs if r[2]==i]) for i in range(1, k+1)])
        min_result = min(min_result, answer)

    return min_result

k = 4
n = 7
reqs = [[10, 60, 1], [15, 100, 3], [20, 30, 1], [30, 50, 3], [50, 40, 1], [60, 30, 2], [65, 30, 1], [70, 100, 2]]
print(solution(k, n, reqs))