def promedio (lista:list): #Se inicializa la funcion con su parametro.
    j=0 #Es una variable que debe iniciar en 0 y se le sumaran los valores de todos los elementos de la lista
    for i in lista: #Permite recorrer todos los elementos de la lista
        j+=i #Toma el valor del componente que se esta tomando para sumarlo a j
    prom=j/len(lista) #Se divide la suma de todos los componenetes (j) entre el numero de elementos para asi conseguir el promedio
    return prom #Hace que la funcion devuelva el valor del promedio calculado.
def multiplicativo (lista:list): #Se inicializa la funcion con su parametro.
    g=1 #Es una variable que debe iniciar en 1 y se le multiplican los valores de todos los elementos de la lista
    for u in lista: #Permite recorrer todos los elementos de la lista
        g*=u #Toma el valor del componente que se esta tomando para multiplicarlo por j
    mult = g**(1/5) #Le saca raiz del radicando de la longitud de la lista (5) a la multiplicacion anterior.
    return mult #Hace que la funcion devuelva el valor del promedio multiplicativo calculado.
def med (lista): #Se inicializa la funcion con su parametro.
    lista.sort() #Ordena la lista de menor a mayor
    valor_med=lista[2] #Toma el valor medio de la lista, al ser una lista de 5 este siempre sera el que se encuentra en la posicion [2]
    return valor_med #Hace que la funcion devuelva el valor de la media calculado.
def orden (lista): #Se inicializa la funcion con su parametro.
    lista.sort() #Ordena la lista de menor a mayor
    return lista #Hace que la funcion devuelva la funcion ordenada de menor a mayor.
def reves (lista): #Se inicializa la funcion con su parametro.
    lista.sort(reverse = True) #Ordena la funcion de mayor a menor.
    return lista #Hace que la funcion devuelva la funcion ordenada de mayor a menor.
def pot_may (lista:list): #Se inicializa la funcion con su parametro.
    lista.sort() #Ordena la lista de menor a mayor
    potencia=lista[len(lista)-1]**lista[0] #Realiza una potencia entre el valor mas grande de la lista elevado al mas pequeño.
    return potencia #Hace que la funcion devuelva el valor de la potencia del mayor elevado al menor calculado.
def raiz (lista:list): #Se inicializa la funcion con su parametro.
    lista.sort() #Ordena la lista de menor a mayor
    cubica=lista[0]**(1/3) #Realiza la operacion de raiz cubica al elemento mas pequeño de la lista.
    return cubica #Hace que la funcion devuelva el valor de la raiz cubica del menor calculado calculado.
if __name__=="__main__":  
    num=5
    lista=[]
    for j in range (0,num):
        lista.append(float(input("escriba un dato")))
    res_prom=promedio(lista)
    print(f"El promedio de los valores de la lista es {res_prom}")
    res_mult=multiplicativo(lista)
    print(f"El promedio multiplicativo de los valores de la lista es {res_mult}")
    res_pot=pot_may(lista)
    print(f"La potencia del numero mas grande de la lista elevado al mas pequeño de la lista es {res_pot}")
    res_rad=raiz(lista)
    print(f"La raiz del valor mas pequeño de la lista es {res_rad}")
    res_med=med(lista)
    print(f"La media de los valores de la lista es {res_med}")
    res_ord=orden(lista)
    print(f"La lista ordenada de menor a mayor es {res_ord}")
    res_rev=reves(lista)
    print(f"La lista ordenada de mayor a menor es {res_rev}")
    

