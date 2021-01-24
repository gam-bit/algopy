
def make_max(n_lst):
    n_max = n_lst[0]

    for i in n_lst[1:]:

        if (n_max * i == 0) | (n_max == 1) | (i == 1):
            n_max += i
        
        else:
            n_max *= i
    
    return n_max

        
        

if __name__ == "__main__":
    n_lst = [int(i) for i in list(input())]
    print(make_max(n_lst))

