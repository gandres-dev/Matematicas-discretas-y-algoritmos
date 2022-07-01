import random
L = [random.randint(1, 10) for _ in range(10)]
print(L)
print(max(L))

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def _radix_aux(L, pos):
    count = [0] * 10
    for m in L:
        aux = m // pos
        print('aux', aux)
    pass


def radix_sort(L):
    L = L.copy()
    pos = 1
    while pos <= max(L):
        print('pos,', pos)
        _radix_aux(L, pos)
        pos *= 10
    return L

L = [random.randint(1, 300) for _ in range(10)]
print(L)
radix_sort(L)


def _radix_aux(L, pos):
    count = [0] * 10
    for m in L:
        aux = m//pos
        count[(aux%10)] += 1
        
    for i in range(1, 10): # Recuperamos las posiciones que nos indica el counting sort
        count[i] += count[i-1]
        
    ordered = [0] * len(L)
    for m in reversed(L):
        aux = m//pos
        ordered[count[aux%10] - 1] = m
        count[aux%10] -= 1
        
    for i in range(len(L)):
        L[i] = ordered[i]

def radix_sort(L):
    L = L.copy()
    pos = 1
    while pos <= max(L):
        _radix_aux(L, pos)
        pos *= 10
    return L
    
radix_sort(Lista)
