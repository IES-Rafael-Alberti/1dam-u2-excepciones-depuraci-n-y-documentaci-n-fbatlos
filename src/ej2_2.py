def impares(numero):
    if numero<1:
        raise ValueError ("Edad menor a 1")
    cuenta=0
    numero+=1
    out=str(" ")
    while numero != 0 :
        cuenta +=1
        if cuenta%2 == 1:
            if numero != 1 :
                out+=str(f" {cuenta} ,")
        numero -=1
    return out
def main():
    numero=None
    while numero==None:
        try:
            numero = int(input("Dame un numero para saber si es impar : "))
            print(impares(numero))
        except ValueError as e:
            print(e)
            numero=None
    


if __name__ == "__main__":
    main()