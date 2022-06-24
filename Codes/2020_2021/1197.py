# https://www.acmicpc.net/problem/1197

def find_parents(parents, x):
    if x != parents[x]:
        parents[x] = find_parents(parents, parents[x])

    return parents[x]



def union_parents(parents, a, b):
    par_a = find_parents(parents, a)
    par_b = find_parents(parents, b)

    if par_a < par_b:
        parents[par_b] = par_a
    else:
        parents[par_a] = par_b


if __name__ == "__main__":

    v, e = map(int, input().split()) 

    parents = [i for i in range(v+1)]
    edges = []
    path = []

    for _ in range(e):
        a, b, c = map(int, input().split()) # node a, node b, cost c
        edges.append((c, a, b))   
        
        
    edges.sort()

    cost = 0

    for e in edges:
        c, a, b = e

        if find_parents(parents, a) != find_parents(parents, b):
            union_parents(parents, a, b)
            cost += c
            path.append(e)


    print(cost)


