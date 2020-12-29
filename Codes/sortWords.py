# https://www.acmicpc.net/problem/1181
# 실버5

# 조건
# 1. 길이가 짧은 것부터
# 2. 사전 순으로
## 같은 단어가 여러 번 입력되면 한 번만 출력
## 입력은 모두 소문자

#--------------------

def sort(words_lst):

    n = len(equal_lst)

    if n == 1:
        return equal_lst

    sort_lst = []
    word_len = len(equal_lst[0])

    for i in range(word_len): # 단어 길이만큼 돌기
        if len(equal_lst) == 1:
            sort_lst = equal_lst
            break

        min_idx = 0
        for j in range(len(equal_lst)): # 단어 하나씩 돌기
            if ord(equal_lst[min_idx][i]) > ord(equal_lst[j][i]):
                min_idx = j
        sort_lst.append(equal_lst[min_idx])
        equal_lst.remove(equal_lst[min_idx])
        print(f"sort_lst: {sort_lst}, equal_lst: {equal_lst}")

    return sort_lst



if __name__ == '__main__':
    n = int(input())

    words = set()
    for _ in range(n):
        words.add(input())
    words = list(words)

    result = sort(words)
    print(result)