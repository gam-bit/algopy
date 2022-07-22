# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    splited_files_dict = {}
    for f in files:
        head = re.search("[^0-9]+", f).group()
        f_new = f[len(head):]
        number = re.search("[0-9]{1,5}", f_new).group()
        tail = f_new[len(number):]
        splited_files_dict[f] = (head, number, tail)
    


if __name__ == "__main__":
    files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(files))