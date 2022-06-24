# https://www.acmicpc.net/problem/1976


def find_parents(x, parents):
    
    if x != parents[x]:
        parents[x] = find_parents(parents[x], parents)

    return parents[x]
    

def union_parents(x, y, parents):
    x = find_parents(x, parents)
    y = find_parents(y, parents)

    if x < y:
        parents[y] = x
    
    else:
        parents[x] = y
 


if __name__ == '__main__':
    
    n = int(input()) # 도시 수
    m = int(input()) # 여행 계획 도시 수(중복 가능)

    parents_lst = [i for i in range(n+1)]
    total_path_lst = []
    for _ in range(n):
        total_path_lst.append(list(map(int, input().split())))
        
    selected_cities = list(set(map(int, input().split())))
    
    for i in range(n):
        for j in range(n):
            if total_path_lst[i][j] == 1:
                union_parents(i+1, j+1, parents_lst)
                print(f"{i+1}과 {j+1}사이의 길 확인 후 parents: {parents_lst}")

               
    flag = set([find_parents(city, parents_lst) for city in selected_cities])

    print(f'parents_lst: {parents_lst}')
    print(f'flag: {flag}')
    if len(flag) == 1:
        print('YES')
    else:
        print('NO')
