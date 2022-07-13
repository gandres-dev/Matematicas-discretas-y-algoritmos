
def forma_lista_con_claves(B, numCar):
    Btmp = []
    D = {}
    j = 0
    for i in range(48, 58):
        D[chr(i)]=j
        j +=1
    for i in range(65, 91):
        D[chr(i)] = j
        j +=1
    for i in range(len(B)):
        Btmp.append([B[i]]*2)
        A3 = list(B[i])
        Btmp[i][1] = D[A3[numCar-1]]
    return Btmp


def contar(A, k):
    C = [0 for _ in range(k+1)]
    B = [list(0 for _ in range(2)) for _ in range(len(A))]
    for j in range(0, len(A)):
        C[A[j][1]] = C[A[j][1]]+1
    for i in range(1, k+1):
        C[i]=C[i]+C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j][1]]-1][1]=A[j][1]
        B[C[A[j][1]]-1][0]=A[j][1]
        C[A[j][1]] = C[A[j][1]]-1

def obtener_elem_sin_claves(E):
    elem = []
    for i in range(0, len(E)):
        elem.append(E[i][0])
    return elem


def radixsort(A):
    numCar = len(A[1])
    for i in range(numCar, 0, -1):
        cc = forma_lista_con_claves(A, i)
        ordenado = contar(cc, 36)
        a = obtener_elem_sin_claves(ordenado)
    return A
