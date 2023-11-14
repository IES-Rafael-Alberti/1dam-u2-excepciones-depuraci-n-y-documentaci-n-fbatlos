def cuenta_atras(numero):
    if numero<1:
        raise ValueError ("ERROR : El número no puede ser menor a 1")
    cont=numero
    out=str()
    while numero != -1 :
        if numero != -1 :
            out+=f" {cont} ,"
        cont-=1
        numero-=1
    return out    

def main():
   numero=None
   while numero==None:
        try:
            numero = int(input("Dame numero : "))
            print(cuenta_atras(numero))
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()