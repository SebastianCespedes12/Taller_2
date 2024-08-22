def no_vocales (lista:list)->list:
    nueva_lista=[]
    for i in lista:
        vocales=0
        for j in i:
            if j == "a"or j== "A"or j=="e"or j=="E"or j=="i"or j=="I"or j=="o"or j=="O"or j=="u"or j=="U":
                vocales+=1
                if vocales ==2:
                    nueva_lista.append(i)
                    print(i)
    if nueva_lista == []:
        print("No existe")    
if __name__ == "__main__":
    lista = []
    num=int(input("Escribe el numero de cadenas que se desean poner:"))
    lista=[]
    for j in range (0,num):
        lista.append(str(input("escriba un dato")))
    cadena=no_vocales(lista)

        