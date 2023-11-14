num=None
while num==None:
    try:
        num=int(input("Dame un número : "))
        print(num)
    except ValueError as e:
        print(e)