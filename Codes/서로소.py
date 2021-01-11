

def find_parents(parents, x): # 경로 압축 방법 -> parents에 최상위 부모 노드가 쓰임
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x] 

def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


v, e = map(int, input().split())

# 부모 테이블 초기화
parents = [0] * (v+1)
for i in range(1, v+1):
    parents[i] = i


for _ in range(e):
    a, b = map(int, input().split()) # 간선 정보
    union_parents(parents, a, b)
    print(parents)

for i in range(1, v+1):
    print(find_parents(parents, i), end=' ')

print()

print(parents)