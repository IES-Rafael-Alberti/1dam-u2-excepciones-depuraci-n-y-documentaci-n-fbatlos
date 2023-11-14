def vuelvedad(edad):
    if edad<1:
        raise ValueError ("Edad menor a 1")
    cuenta=0
    edad+=1
    out=str("Tu edad ")
    while edad != 1 :
        cuenta +=1
        out+=str(f"{cuenta}/")
        edad -=1
    print (out)
def main():
    edad=None
    while edad==None:
        try:
            edad = int(input("Edad : "))
            vuelvedad(edad)
        except ValueError as e:
            print("ERROR " + str(e))
            edad=None

if __name__ == "__main__":
    main()