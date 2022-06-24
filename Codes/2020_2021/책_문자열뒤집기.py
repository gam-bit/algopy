# https://www.acmicpc.net/problem/1439
import sys
input = sys.stdin.readline

def make_change_loc(s):
    """
    문자열을 넣으면 숫자가 바뀌는 지점의 index를 알려주는 list 반환

    예) '0001100' -> [0, 3, 5] 
    """
    change_loc = [0]
    for i in range(1, len(s)):

        if (s[i] == '0') & (s[i-1] != '0'):
            change_loc.append(i)
        
        elif (s[i] == '1') & (s[i-1] != '1'):
            change_loc.append(i)
    
    return change_loc



def flip_string(s, change_loc):
    """
    문자열 뒤집기
    """

    start_idx = change_loc[1]
    if len(change_loc) > 2:
        end_idx = change_loc[2]
    else:
        end_idx = len(s)
    
    
    if s[start_idx] == '1':
        after = '0' * (end_idx - start_idx)  
        
    else:
        after = '1' * (end_idx - start_idx)
    

    s = s[:start_idx] + after + s[end_idx:]
    change_loc = make_change_loc(s)

    return s, change_loc
        

if __name__ == '__main__':

    s = input().split()[0]
    change_loc = make_change_loc(s)

    n_flip = 0

    while len(change_loc) != 1:
        
        s, change_loc = flip_string(s, change_loc)
        n_flip += 1

    print(n_flip)


