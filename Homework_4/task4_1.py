# Напишите функцию для транспонирования матрицы

from random import randint as rand

def generate_matrix(size:int) -> list[list]:

    matrix = []
    for _ in range(size):
        matrix.append([rand(1,100) for i in range(size)])

    return matrix


def print_matrix(matrix: list[list]):

    for i in matrix:
        print(i)
    print('\n')


def transposes_matrix(matrix):

    transp_matrix = []
    for i in range(len(matrix)):
        temp_var = []
        for j in range(len(matrix)):
            temp_var.append(matrix[j][i])
        transp_matrix.append(temp_var)
    return transp_matrix


SIZE_MATRIX = 5
matrix = generate_matrix(SIZE_MATRIX)

print('Исходная матрица:')
print_matrix(matrix)

print('Транспонированная матрица:')
print_matrix(transposes_matrix(matrix))