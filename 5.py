#Recursivo
def mcd_recursivo(a:int,b:int)->int: 
  if b==0: #Si b es igual a 0, se retorna a 
    return a
  elif a==0: #Si a es igual a 0, se retorna b
    return b
  else:
    return mcd_recursivo(b,a%b) #Se retorna la funcion mcd_recursivo con los valores de b y el residuo de a entre b
  
def mcm1(a:int ,b:int)->int: 
  if a == 0: #Si a es igual a 0, se retorna b
    return b
  elif b == 0: #Si b es igual a 0, se retorna a
    return a
  else:
    mcd_ab = mcd_recursivo(a,b) #Se obtiene el mcd de a y b
    return a*b // mcd_ab #Se retorna el producto de a y b entre el mcd de a y b
  
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
  
def mcm2(a:int,b:int)->int:
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
  print(f"el MCM de {a} y {b} es: {mcm1(a,b)}")
  
  a= int(input("Ingrese un numero: ")) 
  b= int(input("Ingrese otro numero: "))
  print(f"el MCM de {a} y {b} es: {mcm2(a,b)}")