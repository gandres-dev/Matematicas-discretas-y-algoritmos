

def count_word(word, a=[],i=-1, candidatos=[], sols=0):
    """
    Cuenta cuántas oraciones diferentes puede formar la string en cuestión suponiendo
    que las únicas palabras que existen son las del conjunto inicial
    """    
    if i >= len(word)-1:
        # La segmentacion esta completa la guardas
        print(a)
        return 1
    
    candidatos = [word[i:j] for j in range(i+1, len(word)+1)]
    for k, c in enumerate(candidatos):                
        a.append(c)
        sols = count_word(word, a, i+k, sols)
        a.remove(c)
    pass    

string = 'holamundo'
count_word(string)
