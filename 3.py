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