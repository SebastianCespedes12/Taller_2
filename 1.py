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