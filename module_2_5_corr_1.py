def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    if m <= 0:
        matrix = []
    return matrix




matr_1 = get_matrix(4,3,11)
matr_2 = get_matrix(5,5,33)
matr_3 = get_matrix(6,2,44)
print(matr_1)
print(matr_2)
print(matr_3)