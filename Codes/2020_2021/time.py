
## <시각>
## 2020-12-24
## 난이도 1
## 풀이시간 15분
## 시간 제한 2초 | 메모리 제한 128MB


n = int(input()) 
cnt = 0

for h in range(n+1):
    # h에 3이 들어가는 경우
    if '3' in str(h): 
        cnt += 60*60
    # h에 3이 안 들어가는 경우
    else:    
        for m in range(60): 
            if '3' in str(m):
                cnt += 60
            else:
                for s in range(60):
                    if '3' in str(s):
                        cnt += 1

print(cnt)

#----------------------------------------
# 정답
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

                        
