# https://programmers.co.kr/learn/courses/30/lessons/92334

from collections import defaultdict

def solution(id_list, report, k):

    report_dict = defaultdict(set)
    reported_dict = defaultdict(set)
    
    for r in report:
        a, b = r.split()
        report_dict[a].add(b)
        reported_dict[b].add(a)
        
    stopped_names = [reported_name for reported_name, nameset in reported_dict.items() if len(nameset) >= k]
    answer = []

    for i in id_list:
        result = [1 for n in stopped_names if n in report_dict[i]]
        answer.append(sum(result))

    return answer

#---------------------------------------------
def optim_solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer
#---------------------------------------------


if __name__ == "__main__":
    import time 

    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    
    start = time.time()
    print(solution(id_list, report, k))
    print(f"Time: {time.time()-start}sec")