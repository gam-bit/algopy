# p.382

# A문자열 -> B문자열
# insert, remove, replace
# 최소편집거리

    

a = input()
b = input()

memo = [[0] * (len(b)+1) for _ in range(len(a)+1)]

memo[0] = [i for i in range(len(b)+1)]
for i in range(1, len(a)+1):
    memo[i][0] = i

for i in range(1, len(a)+1): 
    for j in range(1, len(b)+1): 
        if a[i-1] == b[j-1]:
            memo[i][j] = memo[i-1][j-1]
        else:
            memo[i][j] = 1 + min(memo[i-1][j-1], memo[i][j-1], memo[i-1][j])
        
print(memo[-1][-1])
for row in memo:
    print(row)