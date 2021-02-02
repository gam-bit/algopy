# https://programmers.co.kr/learn/courses/30/lessons/60062


# while weak is not empty:
    # dist에서 거리가 긴 친구의 dist 뽑기
    # while 친구 dist > 0:
    # start_loc와 dist[len(weak)-1] 사이의 거리 구하기(짧은 쪽)
    # end_loc와 dist[0] 사이의 거리 구하기(짧은 쪽)
        # 두 거리 비교해서 더 짧은 쪽으로 start or end를 update하기
        # 해당 거리가 남은 친구 dist보다 크면 친구 제거하고 break
        # 아니면 
            # weak에서 업데이트한 노드 빼기
            # 해당 친구의 dist에서 거리만큼 빼기 

def solution(n, weak, dist):

    dist.sort(reverse=True) # 내림차순 정리

    result = 0
    while (weak != []) and (dist != []):
        f_dist = dist[0] # 거리가 제일 큰 친구 뽑기 - 위에서 내림차순 정리했음
        dist.remove(f_dist)
        result += 1

        print(f"weak: {weak}")
        print(f"dist: {dist}")
        print(f"친구 수 : {result}")
        print(f"f_dist : {f_dist}")
        
        start_loc = weak[0]
        end_loc = weak[0]
        weak.remove(weak[0])

        while (f_dist > 0) and (weak != []):

            # start_loc이랑 가까운 쪽 -> weak[len(weak)-1]
            reverse_clockwise_wall = weak[len(weak)-1]
            dist_start1 = (start_loc - reverse_clockwise_wall) % n
            dist_start2 = (reverse_clockwise_wall - start_loc) % n
            dist_start = min(dist_start1, dist_start2)
            # end_loc이랑 가까운 쪽 -> weak[0]
            clockwise_wall = weak[0]
            dist_end1 = (end_loc - clockwise_wall) % n
            dist_end2 = (clockwise_wall - end_loc) % n
            dist_end = min(dist_end1, dist_end2)

            if min(dist_start, dist_end) > f_dist:
                break
            else:
                if dist_start <= dist_end:
                    start_loc = reverse_clockwise_wall
                    f_dist -= dist_start
                    weak.remove(reverse_clockwise_wall)

                else:
                    end_loc = clockwise_wall
                    f_dist -= dist_end
                    weak.remove(clockwise_wall)
    
    if (dist == []) and (weak != []):
        return -1

    return result

if __name__ == "__main__":
    n = int(input()) # 외벽 길이 
    weak = list(map(int, input().split())) # 취약 지점 위치
    dist = list(map(int, input().split())) # 사람별 1시간동안 이동할 수 있는 거리
    dist.sort(reverse=True) # 내림차순 정리
    print(solution(n, weak, dist))