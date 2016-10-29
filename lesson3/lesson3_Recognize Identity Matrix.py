# By Ashwath from forums
# Given a list of lists representing a n * n matrix as input, 
# define a  procedure that returns True if the input is an identity matrix 
# and False otherwise.

# An IDENTITY matrix is a square matrix in which all the elements 
# on the principal/main diagonal are 1 and all the elements outside 
# the principal diagonal are 0. 
# (A square matrix is a matrix in which the number of rows 
# is equal to the number of columns)

def is_identity_matrix(matrix):
    size0 = len(matrix)
    if size0 == 0:
        return False
    size1 = len(matrix[0])
    if size0 != size1:
        return False

    for j in range(size0):
        for i in range(size1):
            if i == j:
                if matrix[i][i] != 1:
                    return False
            else:
                if matrix[j][i] != 0:
                    return False
    return True
