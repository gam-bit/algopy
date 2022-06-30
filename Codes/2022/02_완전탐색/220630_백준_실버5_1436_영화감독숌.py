# 브루트포스
# https://www.acmicpc.net/problem/1436


n = int(input())

end_num_str = '666'

i = 1
end_num_list = []

while True:
    if len(end_num_list) == n:
        print(end_num_list.pop())
        break
    if end_num_str in str(i):
        end_num_list.append(i)
    i += 1