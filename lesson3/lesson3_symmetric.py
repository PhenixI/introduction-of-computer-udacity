def symmetric(l):
    m = len(l)
    if m==0:
        return True
    n = len(l[0])
    if(n != m):
        return False
    listSize = m
    for i in range(listSize):
        for j in range(listSize):
            if l[j][i] != l[i][j]:
                return False
    return True
