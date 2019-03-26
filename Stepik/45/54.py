def find(n):
    print (n,end=' ')
    if n == 1:
        return n
    elif n%2 == 0:
        n = int(n/2)
    else:
        n = n*3 + 1
    find(n)
    return n

n = int(input())
find (n)