def fac(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    return factorial


def input_matrix(n, m):
    mat = []
    for i in range(n):
        row = [int(el) for el in input(f"Пліз, уведіть {i + 1}-ий рядок\n--> ").split()]
        assert len(row) == m, f"Ви ввели некоректні дані, рядок повинен мати {m} елементів"
        mat.append(row)
    return mat


def print_matrix(mat):
    for row in mat:
        print(row)


def matrix_multiplication(mat1, mat2):
    result = []
    for i in range(len(mat1)):
        row_result = []
        for j in range(len(mat2[0])):
            elem = 0
            for k in range(len(mat2)):
                elem += mat1[i][k] * mat2[k][j]
            row_result.append(elem)
        result.append(row_result)
    return result