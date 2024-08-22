# Taller 2
## **Infinity Bit Team (∞BT)**
* Juan Diego Cárdenas Olarte
* Sebastián Céspedes Rico
* Alejandra Landines Sanabria

[![logo.jpg](https://i.postimg.cc/pdcVKPsT/logo.jpg)](https://postimg.cc/JyJWLCVV)

-------------
>#### 1.Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).

El programa separa los dígitos de un número ingresado utilizando los operadores módulo (%) y división entera (//). El número se procesa dígito por dígito, imprimiendo cada uno desde el primero hasta el ultimo.
```python
def separar_digitos(n:int):
  cantidad: int =len(str(n)) #Se almacena la cantidad de digitos del numero ingresado
  if cantidad==1: #Si el numero ingresado es de un solo
    print(n) #Se imprime el numero ingresado
  else: 
    i: int =1   #Se inicializa la variable i en 1
    while i<=cantidad: #Mientras i sea menor o igual a la cantidad de digitos del numero ingresado
      dig:int =(n//10**(cantidad-i))%10 #Se obtiene el digito de la posicion i
      print(dig, end=" ") #Se imprime el digito
      i+=1 #Se incrementa i en 1
      
if __name__=="__main__":
  n: int = int(input("Ingrese un numero")) 
  separar_digitos(n)
```
>#### 2.Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entregue los dígitos tanto de la parte entera como de la decimal.

La función separa un número flotante en su parte entera y decimal. La parte entera se obtiene con int(), y la parte decimal se calcula restando la parte entera al número original.
```python
def separar_flotante(n:float):
  entero = int(n) #Se obtiene la parte entera del numero
  decimal= n-entero #Se obtiene la parte decimal del numero
  
  return entero, decimal #Se retorna la parte entera y la parte decimal

if __name__=="__main__":
  n: float = float(input("Ingrese un numero")) #Se pide al usuario que ingrese un numero
  entero, decimal = separar_flotante(n) #Se obtiene la parte entera y la parte decimal del numero ingresado
  
  print(f"El numero es: {n}") 
  print(f"La parte entera del numero es: {entero}") #
  print(f"La parte decimal es: {decimal}") 

```
>#### 3.Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos, definiendo números espejos como dos números a y b tales que a se lee de izquierda a derecha igual que se lee b de derecha a izquierda, y viceversa.

El programa invierte un numero mediante una función que extrae sus dígitos uno a uno y los recombina en orden inverso utilizando operadores módulo (%) y división entera (//). Luego, se compara si el número original y el invertido son iguales, determinando si son espejos.
```python 
def invertir(n: int) -> int:
    invertido: int= 0 #Se inicializa la variable invertido en 0
    while n > 0: #Mientras n sea mayor a 0
        invertido = invertido * 10 + n % 10 #Se obtiene el ultimo digito de n y se agrega al numero invertido
        n //= 10 #Se elimina el ultimo digito de n
    return invertido #Se retorna el numero invertido
  
def verificar_espejos(a: int, b: int): 
  invertido_b: int= invertir(b) #Se obtiene el numero b invertido
  if a== invertido_b: #Si a es igual al numero b invertido, se imprime que son numeros espejos
    print("Son numeros espejos") 
  else:  #Si a no es igual al numero b invertido, se imprime que no son numeros espejos
    print("No son numeros espejos")

if __name__ =="__main__":
  a = int(input("Ingrese un numero: "))
  b = int(input("Ingrese otro numero: "))
  verificar_espejos(a,b)
```
>#### 4.Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Calcule con cuántos términos de la serie (i.e: cuáles valores de n), se tienen errores del 10%, 1%, 0.1% y 0.001%.  

El programa calcula el coseno de un número usando la serie de Taylor, sumando los primeros n términos de la serie. Luego, se compara la aproximación con el valor real de la función coseno (usando math.cos()) para determinar el error y cuántos términos son necesarios para alcanzar diferentes niveles de precisión utilizando un bucle y una lista de resultados.
```python
import math

#Función para calcular la aproximación del coseno de un número usando la serie de Taylor.
def cos(x:float,n:int)->float:
    aprox=0 #Variable que almacena la suma de la serie.
    for i in range (n+1): #Itera desde 0 hasta n para sumar a aprox los términos solicitados de la serie.
        nuevo_termino=(((-1)**i)*(x**(2*i)))/math.factorial(2*i) #Calcula el término actual de la serie.
        aprox+=nuevo_termino #Suma el término a la aproximación.
    return aprox #Devuelve la aproximación de coseno de x.

#Función para calcular el número mínimo de términos que se necesitan para obtener ciertos porcentajes de error.
def error(x:float)->float:
    valor_real_cos=math.cos(x) #Math para hallar el valor real de cos(x).
    errores=[10,1,0.1,0.001] #Lista de errores a calcular.
    resultados=[] #Lista para almacenar el número de términos necesarios para cada porcentaje de error.
    for i in errores: #Itera sobre cada uno de los errores a calcular.
        n=1 #El número de términos inicia en 1.
        while True:
            valor_aproximado_cos=cos(x,n) #Calcula la aproximación con n términos.
            error = abs((valor_real_cos-valor_aproximado_cos)/valor_real_cos)*100 #Calcula el error porcentual.
            if error<=i: #Si el error es menor o igual al deseado, se almacena n en la lista de resultados y se sale del ciclo.
                resultados.append(n)
                break
            n+=1 #Incrementa n para probar con un término más.
    return resultados #Devuelve la lista con el número mínimo de términos que se necesitan para obtener los errores solicitados.

if __name__=="__main__": 
    #Se solicita al usuario un valor para x y n.
    x=float(input("Ingrese un número: "))
    n=int(input("¿Cuántos términos de la serie de Taylor desea utilizar para la aproximación?: "))
    
    #Calcula el valor real y aproximado de coseno con las respectivas funciones.
    real=math.cos(x)
    aproximado=cos(x,n)

    #Muestra el valor aproximado, el real y el error porcentual.
    print("Valor aproximado de cos(x): ", aproximado)
    print("Valor real de cos(x): ", real)
    print("Porcentaje de error del valor aproximado: ", abs((real-aproximado)/real)*100,"%")

    #Calcula y muestra el número de términos necesarios para alcanzar los diferentes porcentajes de error.
    print("Si desea un porcentaje de error menor, intente: ")
    print("Para un porcentaje de error menor al 10%, utilice: ", error(x)[0], "términos de la serie")
    print("Para un porcentaje de error menor al 1%, utilice: ", error(x)[1], "términos de la serie")
    print("Para un porcentaje de error menor al 0.1%, utilice: ", error(x)[2], "términos de la serie")
    print("Para un porcentaje de error menor al 0.001%, utilice: ", error(x)[3], "términos de la serie")
```
>#### 5.Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva.

El programa utiliza el Algoritmo de Euclides para calcular el Máximo Común Divisor (MCM) de dos números, y luego aplica la relación entre MCD y MCM, el producto del MCD de dos numeros por el MCM es igual al producto de ambos números. Se implementan tanto versiones recursivas como iterativas del cálculo.
#### Recursivo:
```python
#Recursivo
def mcd_recursivo(a:int,b:int)->int: 
  if b==0: #Si b es igual a 0, se retorna a 
    return a
  elif a==0: #Si a es igual a 0, se retorna b
    return b
  else:
    return mcd_recursivo(b,a%b) #Se retorna la funcion mcd_recursivo con los valores de b y el residuo de a entre b
  
def mcm(a:int ,b:int)->int: 
  if a == 0: #Si a es igual a 0, se retorna b
    return b
  elif b == 0: #Si b es igual a 0, se retorna a
    return a
  else:
    mcd_ab = mcd_recursivo(a,b) #Se obtiene el mcd de a y b
    return a*b // mcd_ab #Se retorna el producto de a y b entre el mcd de a y b

if __name__ == "__main__":
  a= int(input("Ingrese un numero: ")) 
  b= int(input("Ingrese otro numero: "))
  print(f"el MCM de {a} y {b} es: {mcm(a,b)}")
```
#### Iterativo:
```python
#Iterativo
def mcd_iterativo(a:int,b:int)->int:
  if b==0: #Si b es igual a 0, se retorna a
    return a
  elif a==0: #Si a es igual a 0, se retorna b
    return b
  else: 
    while b !=0: #Mientras b sea diferente de 0
      a,b = b,a%b  #Se intercambian los valores de a y b, y b toma el valor del residuo de a entre b
    return a # Se retorna a cuando b sea igual a 0
  
def mcm(a:int,b:int)->int:
  if a == 0:  #Si a es igual a 0, se retorna b
    return b
  elif b == 0: #Si b es igual a 0, se retorna a
    return 
  else:
    mcd_a_b= mcd_iterativo(a,b) #Se obtiene el mcd de a y b
    return a*b // mcd_a_b #Se retorna la division entera del producto de a y b entre el mcd de a y b

if __name__ == "__main__":
  a= int(input("Ingrese un numero: "))
  b= int(input("Ingrese otro numero: "))
  print(f"el MCM de {a} y {b} es: {mcm(a,b)}")
```
>#### 6.Desarrollar un programa que determine si en una lista existen o no elementos repetidos. Pista: Maneje valores booleanos y utilice el operador in. 

Se recorre la lista contando cuántas veces aparece cada elemento, si algún elemento aparece más de una vez, el programa indica que hay elementos repetidos; de lo contrario, indica que no los hay.
```python 
def elementos_repetidos(lista): 
  for i in lista : #Se recorre la lista
    repetido=False  # Se inicializa la variable repetido en False
    if lista.count(i)>1: # Si el elemento i se repite mas de una vez en la lista
      repetido=True #Se cambia el valor de la variable repetido a True
      break
  if repetido: #Si la variable repetido es True, se imprime que hay elementos repetidos
    print("Hay elementos repetidos") 
  else: #Sino se imprime que no hay elementos repetidos
    print("No hay elementos repetidos") 

if __name__=="__main__":
  lista = [1,2,4,"a",4] 
  elementos_repetidos(lista) 
```
>#### 7.Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
El programa recorre todos los elementos de una lista, por cada uno de estos recorre a su vez sus caracteres, si el programa detecta que alguno de estos caracteres es una vocal sumara uno a una variable que al llegar a dos hara que se imprima la cadena que se esta tomando. Si no se encuentra ninguna cadena con mas de dos vocales se imprimira el texto "No existe"
```python 
 #Función que permite saber si una cadenas de texto tiene dos o mas vocales.
def no_vocales (lista:list)->list: #Se inicializa la funcion con sus parametros.
    nueva_lista=[] #Lista de guia que permitira saber si ningun elemento tiene mas de dos vocales.
    for i in lista: #Permite recorrer todos los elementos de la lista
        vocales=0 #Variable bandera
        for j in i: #Permite recorrer cada caracter de la cadena
            if j == "a"or j== "A"or j=="e"or j=="E"or j=="i"or j=="I"or j=="o"or j=="O"or j=="u"or j=="U": #Permite identificar si alguna letra de la cadena es una vocal.
                vocales+=1 #Le suma uno a la variable bandera cuando se cumple la condicion anterior
                if vocales ==2: #Condiciona lo que pasa cuando en una cadena hay dos vocales
                    nueva_lista.append(i) #Añade dicha cadena a la lista de guia
                    print(i) #Si tiene dos o mas vocales imprimira la cadena
    if nueva_lista == []: #Condiciona que pasa si tras la iteracion la lista guia sigue vacia
        print("No existe")  #Si sigue vacia se imprime "no existe"  
if __name__ == "__main__":
    lista = [] 
    num=int(input("Escribe el numero de cadenas que se desean poner:"))
    lista=[]
    for j in range (0,num):
        lista.append(str(input("escriba un dato")))
    cadena=no_vocales(lista)
```
>#### 8.Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. 

El programa compara dos listas y crea una nueva lista con los elementos que están en la primera lista pero no en la segunda, utilizando los operadores `in` y `not`.
```python 
def si_lista1_no_lista2(lista1: list,lista2: list) -> list:   
  lista_result=[] # Se inicializa una lista vacía
  for i in lista1: # Se recorre la lista1
    if i not in lista2: # Si el elemento i de la lista 1 no está en la lista 2
      lista_result.append(i) # Se agrega el elemento i a la lista_result
  return lista_result 

if __name__=="__main__": 
  lista1=[1,2,3,4,5,"a"]
  lista2=[5,3,2,4]
  print(si_lista1_no_lista2(lista1,lista2))
```
>#### 9.Resolver el punto 7 del taller 1 usando operaciones con vectores.
Para hacer esto se hizo uso de 7  funcinoes, la primera de ella iteraba todos los elementos de la lista sumandolos para luego dividirlos entre el largo de la lista para asi ascar el promedio. La segunda funcion tambien iteraba todos los elementos de la lista pero esta vez multiplicandolos para finalmente sacarle la raiz quinta a este resultado. La tercera funcion devolvia el valor medio de la lista, para esto ordenaba los valores de menor a mayor y devolvia siempre el tercero ya que es una lista de 5 elementos. La cuarta funcion hacia uso de la operacion de listas ".sort" para ordenar la lista de menor a mayor y devolverla. La quinta lista hacia uso de la operacin de listas "lista.sort(reverse = True)" para ordenar la lista de mayor a menor. La sexta funcion hace uso de la funcion de listas ".sort" para ordenarla de menor a mayor para asi poder elevar el ultimo de la lista elevado al primero (Mayor elevado al menor). La ultima lista tambien hace uso de la operacion ".sort" para ordenar la lista de menor a mayor para asi poderle sacar raiz cubica al primer elemento de la lista (El mas pequeño)
```python 
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
```
>#### 10.Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad? 

El programa comprueba que cada elemento de la lista se múltiplos de 3 utilizando el operador de modulo (%). Se presentan dos enfoques: un patrón de acumulación y una comprensión de listas. Además, se resuelve el problema sin usar el operador módulo, utilizando parte del codigo del primer punto.
```python 
def acum_mult_tres (A: list) -> list:
  B=[] #Se inicializa una lista vacía
  for i in A: #Se recorre la lista A
    if i%3==0: #Si el elemento i de la lista A es multiplo de 3
      B.append(i) #Se agrega el elemento i a la lista B
  return B

def compr_mult_tres(A: list) -> list:  
  B=[i for i in A if i%3==0] #Se crea una lista B con los elementos de la lista A que son multiplos de 3
  return B

if __name__=="__main__":  
  A=[1,2,3,4,5,6,7,8,9,10]
  print(acum_mult_tres(A))
  print(compr_mult_tres(A))
```
```python
#Desafio:

def sumar_digitos(n:int)->int:
  cantidad= len(str(n))  #Se almacena la cantidad de digitos del numero ingresado
  if cantidad == 1: #Si el numero ingresado es de un solo digito
    return n
  elif n>0:
    i: int =1   #Se inicializa la variable i en 1
    sum=0       #Se inicializa la variable sum en 0
    while i<=cantidad: #Mientras i sea menor o igual a la cantidad de digitos del numero ingresado
      dig:int =(n//10**(cantidad-i))%10 #Se obtiene el digito de la posicion i
      sum+=dig #Se suma el digito a la variable sum
      i+=1 #Se incrementa i en 1 
  return sumar_digitos(sum) # Se retorna la suma de los digitos hasta que sea de un solo digito

def acum_mult_tres(A: list) -> list: 
  B=[]  #Se inicializa una lista vacía
  for i in A:  #Se recorre la lista A
    if sumar_digitos(i) in (3,6,9): #Si la suma de los digitos del elemento i de la lista A es 3, 6 o 9
      B.append(i) #Se añade a la lista B
  return B

def compr_mult_tres(A: list) -> list:
  B=[i for i in A if sumar_digitos(i) in (3,6,9)] #Si la suma de los digitos del elemento i de la lista A es 3, 6 o 9 se añade a la lista.
  return B

if __name__=="__main__":
  A=[3223,3253,8775,9336,9999]
  print(compr_mult_tres(A))
  print(acum_mult_tres(A))
```
>#### 11.Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

El programa verifica si la suma de las filas, columnas y diagonales es igual. Lo hace sumando los elementos de las filas, columnas y diagonales y comparándolos con la suma de referencia (la primera fila).
```python 
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
```
