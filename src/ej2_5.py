contrase=None
while contrase==None:
    try:
        contrase=(input("Dame tu contraseña : "))
        if contrase != "panconpan":
            raise NameError("Incorrect Password!!.")
        print(f"{contrase} es correcta")
    except NameError as e:
        print(e)
        contrase=None