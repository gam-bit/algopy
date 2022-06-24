# https://programmers.co.kr/learn/courses/30/lessons/60062

# 친구가 최대 8명이므로 친구를 나열하는 모든 경우의 수는 8! = 40320가지로 많지않음
# 친구가 나오는 가능한 순서를 모두 나열해놓고 
# 각 상황별로 친구가 몇명씩 필요한지 확인
# 더 적은 친구가 필요한 상황을 update
# 1명만 필요한 경우 break 하고 1 반환

from itertools import permutations

def my_solution(n, weak, dist): # 아래 잘못된 부분때문에 70점
    # 친구가 배열되는 모든 경우의 수
    f_list = list(permutations(dist))
    f_count_list = []

    
    for f in f_list:
        
        f = list(f) 
        weak_list = weak[:]
        f_count = 0
        # print('='*10)
        # print(f)
        # print(weak_list)
        
        # 친구가 없거나 확인할 외벽이 없으면 종료
        while (weak_list != []) and (f != []):
            # 1) 첫번째 위치한 친구 뽑아내고 리스트에서 제거
            f_dist = f[0] 
            f.remove(f_dist)
            f_count += 1
            
            # print(f"weak_list: {weak_list}")
            # print(f"친구 수: {f_count}")
            # print(f"남은 친구: {f}")
            # print()
            
            # 출발 지점과 꼬리 지점을 첫번째 외벽으로 지정하고 해당 외벽 제거
            start_loc = weak_list[0]
            end_loc = weak_list[0]
            weak_list.remove(weak_list[0])

            # 친구가 갈 수 있는 총 거리만큼 이동했거나 외벽이 없으면 
            # while문 종료하고 위의 while문에서 다른 친구 데려오기
            while (f_dist > 0) and (weak_list != []):

                # start_loc이랑 가까운 쪽 -> weak_list[len(weak_list)-1]
                reverse_clockwise_wall = weak_list[len(weak_list)-1]
                dist_start1 = (start_loc - reverse_clockwise_wall) % n
                dist_start2 = (reverse_clockwise_wall - start_loc) % n
                dist_start = min(dist_start1, dist_start2)
                # end_loc이랑 가까운 쪽 -> weak_list[0]
                clockwise_wall = weak_list[0]
                dist_end1 = (end_loc - clockwise_wall) % n
                dist_end2 = (clockwise_wall - end_loc) % n
                dist_end = min(dist_end1, dist_end2)

                # 다음 외벽까지의 거리가 이동할 수 있는 거리보다 멀면 while문 빠져나가기
                if min(dist_start, dist_end) > f_dist:
                    break
                else: # 여기가 문제!!!!!!dist_start == dist_end인 경우 처리해줘야 함! 
                    if dist_start < dist_end: 
                        start_loc = reverse_clockwise_wall
                        f_dist -= dist_start
                        weak_list.remove(reverse_clockwise_wall)

                    elif dist_start >= dist_end:
                        end_loc = clockwise_wall
                        f_dist -= dist_end
                        weak_list.remove(clockwise_wall)
                    
                    # else: # 두 거리가 같을 경우 해결 못함
                    #     pass


        # 외벽만 남은 경우
        if (f == []) and (weak_list != []):
            break
        
        # 
        if f_count == 1:
            return 1
        
        f_count_list.append(f_count)

    if f_count_list == []:
        return -1

    return min(f_count_list)

#------------------------------------
# 모든 친구가 나오는 경우를 완전탐색하는 것은 동일
# ★weak를 원형으로 보지 말고 2배로 늘려서 일자형으로 생각함

def solution(n, weak, dist):

    total_weak_cnt = len(weak)
    weak = weak + [i+n for i in weak]
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화

    # 가능한 시작 지점을 모두 확인
    for start in range(total_weak_cnt):
        # 친구가 나올 수 있는 경우 모두 확인
        for friend in permutations(dist): # permutation은 제너레이터라서 객체를 받아놓고 쓸수 없음
            count = 1 # 투입할 친구 수
            last_position = weak[start] + friend[count-1]
            # print(f"친구 전체: {friend}")
            #★시작점부터 모든 취약지점 확인★
            for idx in range(start, start+total_weak_cnt):
                # 만약 idx가 last_position보다 크면 친구가 필요함
                if weak[idx] > last_position:
                    # print(f'친구 필요함. 친구 끝 위치: {last_position}, 확인할 외벽 위치: {weak[idx]}')
                    count += 1
                    if count > len(dist): # 친구를 다 투입했는데 외벽이 남은 경우
                        # print('남은 친구 없음')
                        break
                    last_position = weak[idx] + friend[count-1]
        
            # print(f"투입 친구 수 :{count}")
            answer = min(answer, count)
    
    if answer > len(dist):
        return -1
    
    return answer


if __name__ == "__main__":
    n = int(input()) # 외벽 길이 
    weak = list(map(int, input().split())) # 취약 지점 위치
    dist = list(map(int, input().split())) # 사람별 1시간동안 이동할 수 있는 거리
    print(solution(n, weak, dist))