# 여행을 떠날 수 있는 그룹 수의 최댓값
# 높은 순서대로 묶기

n = int(input()) # 모험가 수
hero_stats = list(map(int, input().split()))

hero_stats.sort() 

cnt_team = 0
while hero_stats: 

    leader_stat = hero_stats.pop()  
    
    if len(hero_stats) >= leader_stat-1: # 남아 있는 사람 수 >= 뽑아야 하는 팀원 수    
        for i in range(leader_stat-1):
            hero_stats.pop()      
        cnt_team += 1
        
    else:
        hero_stats = []
    
print(cnt_team)