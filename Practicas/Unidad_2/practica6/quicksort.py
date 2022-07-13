
def intercambiar(A, x, y):
    tmp = A[x]
    A[x] = A[y]
    A[y] = tmp

def particionar(A, p, r):
    print(A)
    x = A[p]
    print(x)
    i = p
    for j in range(p+1, r+1):
        if A[j] <= x:
            i += 1
            intercambiar(A, i, j)
    intercambiar(A, i, p)
    return i

def quicksort(A, p, r):
    if p < r:
        q = particionar(A, p, r)
        quicksort(A, p, q-1)
        quicksort(A, q+1, r)

import random 

lista = [random.randint(1, 10) for i in range(10)] 

print(lista)


