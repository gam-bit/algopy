# https://www.acmicpc.net/problem/1181
# 실버5

# 조건
# 1. 길이가 짧은 것부터
# 2. 사전 순으로
## 같은 단어가 여러 번 입력되면 한 번만 출력
## 입력은 모두 소문자

#--------------------


def sort(words_lst):
    
    n = len(words_lst)
    if n <= 1:
        return words_lst
    
    pivot = len(words_lst[0])
    less_lst, equal_lst, more_lst = [], [], []


    for word in words_lst:
        if len(word) > pivot:
            more_lst.append(word)
        elif len(word) < pivot:
            less_lst.append(word)
        else:
            equal_lst.append(word)

    return sort(less_lst) + sort_by_alphabet(equal_lst) + sort(more_lst)


def sort_by_alphabet(equal_lst):

    n = len(equal_lst)

    if n <= 1:
        return equal_lst

    pivot_word = equal_lst[0]

    before_lst, now_lst, after_lst = [], [], []

    for word in equal_lst:
        idx = compare_alpha_idx(pivot_word, word)
        if ord(word[idx]) > ord(pivot_word[idx]):
            after_lst.append(word)
        elif ord(word[idx]) < ord(pivot_word[idx]):
            before_lst.append(word)
        else:
            now_lst.append(word)

    return sort_by_alphabet(before_lst) + now_lst + sort_by_alphabet(after_lst)


def compare_alpha_idx(a, b):
    n = len(a)
    for i in range(n):
        if ord(a[i]) != ord(b[i]):
            return i  # 알파벳이 다른 index
    return -1   # 단어가 같으면 -1 출력


if __name__ == '__main__':
    n = int(input())

    words = set()
    for _ in range(n):
        words.add(input())
    words = list(words)
            

    result = sort(words)
    for i in result:
        print(i)
    