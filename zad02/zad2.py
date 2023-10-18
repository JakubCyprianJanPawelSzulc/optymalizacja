import copy

def printMatrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])

def contains_C3_naive(adj_matrix):
    for i in range(0, len(adj_matrix)):
        for j in range(0, len(adj_matrix)):
            if adj_matrix[i][j] == 1:
                for k in range(0, len(adj_matrix)):
                    if adj_matrix[j][k] == 1 and adj_matrix[k][i] == 1:
                        print("Cykl C3 znaleziony w: " + str(i) + " " + str(j) + " " + str(k))
                        return True
    return False

def matrix_to_power_3(matrix):
        a = matrix
        c = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
        d = copy.deepcopy(c)
        for i in range(len(a)):
            for j in range(len(a[0])):
                for k in range(len(a)):
                    c[i][j] += a[i][k] * a[k][j]
        for i in range(len(a)):
            for j in range(len(c[0])):
                for k in range(len(c)):
                    d[i][j] += a[i][k] * c[k][j]
        matrix = d
        return d
    
def contains_C3_matrix_multiplication(adj_matrix):
    exponentiated_matrix = matrix_to_power_3(adj_matrix)
    helper = 0
    for i in range(0, len(exponentiated_matrix)):
        helper += exponentiated_matrix[i][i]
    print("Liczba cykli C3: " + str(helper/6))
    return True if helper > 0 else False
    


def main():
    matrix2=[[0,1,1,0],
             [1,0,1,0],
             [1,1,0,0],
             [0,0,0,0]]
    matrix3=[[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]]
    

    print(contains_C3_naive(matrix2))
    print(contains_C3_matrix_multiplication(matrix2))
    
    print("--------------------")

    print(contains_C3_naive(matrix3))
    print(contains_C3_matrix_multiplication(matrix3))

    

if __name__ == "__main__":
    main()

