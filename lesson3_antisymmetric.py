def antisymmetric(A):
    size = len(A)
    if size == 0:
        return True
    size2 = len(A[0])
    if size != size2:
        return False
    for i in range(size):
        for j in range(size):
            if A[i][j] != -A[j][i]:
               return False
    return True
