try:
    x= 10
    y= 20
    z= x+y
    print(a)
except ZeroDivisionError:
    print("Error de division")
except TypeError:
    print("Ha ocurrido un error de tipo de dato")
except Exception as e:
    print(e)

