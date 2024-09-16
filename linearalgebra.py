import numpy as np
import sympy as sym

def RREF():
    A = np.loadtxt("A.txt", dtype='int')
    (Arrefmatrix, Arrefpivots) = sym.Matrix(A).rref()
    print("The reduced row echelon form of matrix A:")
    print(np.array(Arrefmatrix))
    print("The pivots of matrix A:")
    print(np.array(Arrefpivots))

def symbolicrref():
    s,t = sym.symbols('s, t')
    A = sym.Matrix(2,3, [2,-1, s, 1, -1/2, t])
    A_echelon_form = sym.Matrix(A).echelon_form()
    print("An echelon form of matrix A:")
    print(np.array(A_echelon_form))

if __name__ == '__main__':
    print("Hello Linear Algebra Fans!")
    print("What do you want to do?")
    print("1. Compute the RREF of the matrix A")
    print("2. Compute an echelon form of the symbolic matrix A")
    option = input()
    if (option == "1"):
        RREF()
    elif (option == "2"):
        symbolicrref()

#print(type(B))
#C = np.linalg.matmul(A,B)
# Rank of a matrix
#print("Rank of A:", np.linalg.solve(A,C))
