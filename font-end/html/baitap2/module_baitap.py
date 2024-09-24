# module bài 1
import math
def bac1(a,b):
    return -b / a

def delta(a,b,c):
    return b*b - 4*a*c

def nghiemkep(a,b):
    return -b/2*a

def x1(a,b,delta):
    return (-b + math.sqrt(delta)) / 2*a

def x2(a,b,delta):
    return (-b - math.sqrt(delta)) / 2*a

# module bài 2
def nhan2matran(matrix1, matrix2):
    ketqua = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        ketqua.append(row)
    return ketqua

def matranchuyenvi(matrix):
    ketqua = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return ketqua

def cong2matran(matrix1, matrix2):
   ketqua = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
   return ketqua

