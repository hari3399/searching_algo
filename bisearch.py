

def binsearch(ls, key):
    h = len(ls) - 1
    l = 0
    m = (l + h) // 2

    while l <= h:
        m = (l + h) // 2
        if ls[m] == key:
            return m
        elif ls[m] < key:
            l = m + 1
            
        else:
            h = m - 1
            
    return -1

if __name__ == '__main__':
    ls = [1, 3, 5, 6, 11, 12, 34, 55, 66, 88]
    key = 66

    result = binsearch(ls, key)
    print(result)


             
