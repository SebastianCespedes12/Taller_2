# Taller_2
>#### 1.Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número. Pista: Utilice los operadores módulo (%) y división entera (//).
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
```python 
 
```
>#### 5.Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde una perpectiva tanto iterativa como recursiva. Pista: Puede ser de utilidad chequear el Algoritmo de Euclides para el cálculo del Máximo Común Divisor, y revisar cómo se relaciona este último con el Mínimo Común Múltiplo.
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
```python 
 
```
>#### 8.Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista. 
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
```python 
 
```
>#### 10.Suponga que se tiene una lista A con ciertos números enteros. Desarrolle una función que, independientemente de los números que se encuentran en la lista A, tome aquellos números que son múltiplos de 3 y los guarde en una lista nueva, la cual debe ser retornada por la función. Implemente la perspectiva de un patrón de acumulación y también de comprensión de listas. Desafío: Si ya lo logró, inténtelo ahora sin utilizar el módulo (%). Pista: Un número es multiplo de 3 si la suma de sus dígitos también lo es, ¿verdad? 
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
  cantidad= len(str(n)) 
  if cantidad == 1: #Si el numero ingresado es de un solo digito
    return n
  elif n>0:
    #Se almacena la cantidad de digitos del numero ingresado
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
      B.append(i)
  return B

def compr_mult_tres(A: list) -> list:
  B=[i for i in A if sumar_digitos(i) in (3,6,9)]
  return B

if __name__=="__main__":
  A=[3223,3253,8775,9336,9999]
  print(compr_mult_tres(A))
  print(acum_mult_tres(A))
```
>#### 11.Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
```python 
 
```
