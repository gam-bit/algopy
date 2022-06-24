
## <큰 수의 법칙>
## 2020-12-23
## 난이도 1
## 풀이시간 30분
## 시간 제한 1초 | 메모리 제한 128MB


# n : 2이상 1,000이하 자연수 - 배열의 크기
# m : 1이상 10,000이하 자연수 - 숫자가 더해지는 횟수
# k : 1이상 10,000이하 자연수 - 연속해서 k번을 초과하여 더할 수 없음
# k <= m


def LawOfLargeNumbers(lst, m, k):
    lst.sort()
    v_first = lst[-1]
    v_second = lst[-2]
    
    bag = [0]
    
    while len(bag) < m+1:
        if bag[-1] != v_first:
            bag += [v_first] * k
        else:
            bag += [v_second]
    
    return sum(bag[:m+1])



if __name__ == '__main__':
    n, m, k = map(int, input().split(' '))
    lst = list(map(int, input().split(' ')))
    print(LawOfLargeNumbers(lst, m, k))









