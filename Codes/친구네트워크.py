# https://www.acmicpc.net/problem/4195


def find_team(team, a):
    if team[a] != a:
        team[a] = find_team(team, team[a])
    return team[a]


def union_team(team, a, b):
    team_a = find_team(team, a)
    team_b = find_team(team, b)

    if team_a < team_b:
        team[team_b] = team_a
    else:
        team[team_a] = team_b




n = int(input())
result = []
for _ in range(n):
    r_num = int(input())

    f_net = {}
    team = []
    for i in range(r_num):
        f1, f2 = input().split()


        if f1 not in f_net.keys() and f2 not in f_net.keys():
            f_net[f1] = len(team)
            f_net[f2] = len(team) + 1 
            team += [len(team)] * 2


        elif f1 not in f_net.keys():
            f_net[f1] = len(team)
            team += [len(team)]

        elif f2 not in f_net.keys():
            f_net[f2] = len(team)
            team += [len(team)]
  
        union_team(team, f_net[f1], f_net[f2])
        
        k = find_team(team, team[f_net[f1]])
        cnt = 0
        for i in range(len(team)):
            if k == find_team(team, i):
                cnt += 1

        result.append(cnt)
        
        

for r in result:
    print(r)