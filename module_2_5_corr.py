def get_matrix(n,m,value):
    matrix = []
    matrix_ = []
    if m <= 0 or n <= 0:
        print('Error: Enter a positive number')
    else:
        for j in range(m):
                matrix_.append(value)
        for i in range(n):
                matrix.append(matrix_)
        return matrix


matr_1 = get_matrix(3,4,11)
matr_2 = get_matrix(5,5,33)
matr_3 = get_matrix(6,2,44)
print(matr_1)
print(matr_2)
print(matr_3)