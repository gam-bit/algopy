# https://www.acmicpc.net/problem/15686
from itertools import combinations

def mht_dist(building_loc1, building_loc2):
    """
    두 건물의 위치를 입력하면
    두 건물 사이의 맨하탄 거리를 출력하는 함수
    """
    r1, c1 = building_loc1
    r2, c2 = building_loc2
    return abs(r1-r2) + abs(c1-c2)

def make_loc_house_and_chicken(citymap):
    """
    도시 지도를 넣으면 
    집과 치킨집의 위치를 출력
    """
    houses = []
    chickens = []

    for i in range(len(citymap)): # row
        for j in range(len(citymap[i])): # col
            if citymap[i][j] == 1:
                houses.append((i, j))
            elif citymap[i][j] == 2:
                chickens.append((i, j))
    
    return houses, chickens


def make_chicken_dist_of_house(houses, chickens):
    """
    집과 치킨집의 위치를 알려주는 리스트를 입력하면
    각 집마다 치킨 거리를 구해서 list로 반환
    """
    
    chicken_dist_lst = []
    for h_loc in houses:
        dist = 1e9 # 최대값으로 설정
        for ch_loc in chickens:
            new_dist = mht_dist(h_loc, ch_loc)
            if dist > new_dist:
                dist = new_dist
        chicken_dist_lst.append(dist)
    
    return chicken_dist_lst


if __name__=="__main__":
    
    n, m = map(int, input().split()) # m <= 치킨집 개수 <= 13

    citymap = []
    for i in range(n):
        citymap.append(list(map(int, input().split())))

    # 집, 치킨집 위치
    houses, chickens = make_loc_house_and_chicken(citymap)

    # 치킨집을 원하는 개수만큼 뽑은 모든 상황 확인
        # 집집마다 치킨 거리를 추출해서 list에 모은 뒤에 sum하여 도시의 치킨 거리 구하기
        # 도시 치킨 최솟값으로 업데이트하기

    allcase = list(combinations(chickens, m))

    min_dist = 1e9 
    for i in allcase:
        m_chickens = list(i)
        min_val = sum(make_chicken_dist_of_house(houses, m_chickens))
        if min_dist > min_val:
            min_dist = min_val

    print(min_dist)