def multiply_matrix(m1, m2):
    '''
    Multiplication of the 2 matricies m1 and m2
    '''
    result = [[0 for j in range(len(m2[0]))] for i in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                result[i][j] += m1[i][k] * m2[k][j]
    return result