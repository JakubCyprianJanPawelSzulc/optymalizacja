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

def matrix_exponentation(matrix1):
    matrix2 = [[0 for x in range(len(matrix1))] for y in range(len(matrix1))]
    for i in range(0, len(matrix1)):
        for j in range(0, len(matrix1)):
            for k in range(0, len(matrix1)):
                matrix2[i][j] += matrix1[i][k] * matrix1[k][j]
    return matrix2
    
def contains_C3_matrix_multiplication(adj_matrix):
    exponentiated_matrix = matrix_exponentation(adj_matrix)
    for i in range(0, len(exponentiated_matrix)):
        for j in range(0, len(exponentiated_matrix)):
            if exponentiated_matrix[i][j] > 0:
                for k in range(0, len(exponentiated_matrix)):
                    if adj_matrix[j][k] == 1 and adj_matrix[k][i] == 1:
                        print("Cykl C3 znaleziony w: " + str(i) + " " + str(j) + " " + str(k))
                        return True
    return False


def main():
    matrix=[[0,1,0,0,0,0],
            [1,0,1,0,0,0],
            [0,1,0,1,0,0],
            [0,0,1,0,1,0],
            [0,0,0,1,0,1],
            [0,0,0,0,1,0]]
    
    print(contains_C3_naive(matrix))
    print(contains_C3_matrix_multiplication(matrix))

    

if __name__ == "__main__":
    main()

