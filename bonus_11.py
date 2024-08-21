#Función para saber si una matriz es mágica.
def matriz_magica(matriz:list)->bool:

    filas = len(matriz) #Obtiene el número de filas/columnas de la matriz (asumimos que es cuadrada).
    
    #Calcula la suma de los elementos de la primera fila para usarla como referencia.
    suma_primer_fila=0
    for i in range (filas):
        suma_primer_fila+=matriz[0][i]

    #Calcula la suma de los elementos para cada fila.
    for i in range (filas):
        suma_fila=0
        for j in range (filas):
            suma_fila+=matriz[i][j]
        #print(suma_fila)

        #Si la suma de la fila actual no es igual a la suma de referencia ya se sabe que la matriz no es mágica y se retorna un False.
        if suma_fila!=suma_primer_fila:
            return False
    
    #Calcula la suma de los elementos para cada columna.
    for i in range (filas):
        suma_columna=0
        for j in range (filas):
            suma_columna+=matriz[j][i]
        #print(suma_columna)

        #Si la suma de la columna actual no es igual a la suma de referencia ya se sabe que la matriz no es mágica y se retorna un False.
        if suma_columna!=suma_primer_fila:
            return False
    
    #Verifica que la suma de la diagonal proncipal sea igual a la suma de referencia.
    suma_diagonal=0
    for i in range(filas):
        suma_diagonal+=matriz[i][i]
    #print(suma_diagonal)
    if suma_diagonal!=suma_primer_fila:
        return False
    
    #Verifica que la suma de la diagonal secundaria sea igual a la suma de referencia.
    suma_otra_diagonal=0
    for i in range(filas):
        suma_otra_diagonal+=matriz[i][(filas-1)-i]
    #print(suma_otra_diagonal)
    if suma_otra_diagonal!=suma_primer_fila:
        return False
    
    return True #Si todas las condiciones se cumplen, la matriz es mágica.
    
if __name__=="__main__": 
    matriz=[[17,24,1,8,15],[23,5,7,14,16],[4,6,13,20,22],[10,12,19,21,3],[11,18,25,2,9]]
    magica=matriz_magica(matriz) #Se evalua la función matriz_magica enviando como argumento la matriz de arriba.

    #Imprime si la matriz es mágica o no.
    if magica==True:
        print("La matriz es mágica")
    else:
        print("La matriz no es mágica")