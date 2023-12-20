
print("Hola Mundo")
print("Hola Mundo")
print ('hola mundo')
number = 10
print(number)

if number >= 10:
    if number <10:
        print('es un numero menor')#El tab es importante para que se ejecute
    print('es un numero mayor o igual a 10')
print('fuera')

lista = [1,2,3,4,'5','hola','false',8,9,10]
print(lista)
lista.append('agregado')
print(lista)
tupla = (1,2,3,4,'5','hola','false',8,9,10)
print(tupla)#no se puede modificar

print(lista[0])
diccionario = {'nombre':'jose','apellido':'perez','edad':20}
print(diccionario['apellido'])

for i in range(10):
    print(i)

for i in range(len(lista)):
    print(lista[i])

print()#salto de linea
for each in lista:
    print(each)

print()#salto de linea
for each in diccionario:
    print(each)

print()#salto de linea
users= [
    {
        'nombre':'jose',
        'apellido':'perez',
        'edad':20,
        },
        {'nombre':'pepe',
        'apellido':'torres',
        'edad':23,
        }
]
for each in users:
    print(each['nombre'])