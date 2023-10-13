def generateMatrix(a, b):
    return [[0 for x in range(a)] for y in range(b)]

def printMatrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])

def addEdge(matrix, v1, v2):
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1


def removeEdge(matrix, v1, v2):
    matrix[v1][v2] = 0
    matrix[v2][v1] = 0

def addVertex(matrix):
    for i in matrix:
        i.append(0)
    matrix.append([0] * len(matrix[0]))


def removeVertex(matrix, v):
    matrix.pop(v)
    for i in matrix:
        i.pop(v)

def getVertexDegree(matrix, v):
    return sum(matrix[v])

def getMinGraphDegree(matrix):
    return min(list(map(lambda row: sum(row), matrix)))

def getMaxGraphDegree(matrix):
    return max(list(map(lambda row: sum(row), matrix)))

def getEvenVertex(matrix):
    return len([num for num in list(map(lambda row: sum(row), matrix)) if num % 2 == 0])

def getOddVertex(matrix):
    return len([num for num in list(map(lambda row: sum(row), matrix)) if num % 2 != 0])

def getEdgeListSorted(matrix):
    return sorted(list(map(lambda row: sum(row), matrix)), reverse=True)

def main():
    m1=generateMatrix(6,6)
    printMatrix(m1)
    addEdge(m1, 0, 1)
    addEdge(m1, 0, 2)
    addEdge(m1, 1, 2)
    print("macierz po dodaniu krawedzi")
    printMatrix(m1)
    removeEdge(m1, 0, 1)
    print("macierz po usunieciu krawedzi")
    printMatrix(m1)
    addVertex(m1)
    print("macierz po dodaniu wierzcholka")
    printMatrix(m1)
    removeVertex(m1, 1)
    print("macierz po usunieciu wierzcholka")
    printMatrix(m1)
    print("stopien wierzcholka 0")
    print(getVertexDegree(m1, 0))
    print("minimalny stopien grafu")
    print(getMinGraphDegree(m1))
    print("maksymalny stopien grafu")
    print(getMaxGraphDegree(m1))
    print("liczba wierzcholkow parzystych")
    print(getEvenVertex(m1))
    print("liczba wierzcholkow nieparzystych")
    print(getOddVertex(m1))
    print("posortowana lista stopni wierzcholkow")
    print(getEdgeListSorted(m1))

if __name__ == "__main__":
    main()