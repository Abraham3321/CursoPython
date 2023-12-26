
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

if users[0]['nombre'] == 'jose':
    print('es jose')
elif users[0]['nombre'] == 'pepe':
    print('es pepe')
else:
    print('no es jose')

#switch= { no existe en python solo con diccionarios
#   1: print('hola'),
#  2: print('mundo'),
#  3: print('!')
#}

def saludar():
    print('hola mundo')

def suma(number_one, number_two):
    result= number_one + number_two 
    print(result)

saludar()
suma(10,20)

def __init__(self, nombre, salario):
    self.nombre = nombre
    self.salario = salario

def obtener_nombre(self):
    return f"Nombre: {self.nombre}, Salario: {self.salario}"



class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_nombre(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}"


    def aumentar_salario(self, porcentaje):
        aumento = self.salario * porcentaje / 100
        self.salario += aumento
        return self.salario
    
Empleado1 = Empleado('Jose', 500)
print(Empleado1.obtener_nombre())
Empleado2 = Empleado('Pepe', 1000)
print(Empleado2.obtener_nombre())

print(Empleado1.aumentar_salario(10))
print('------------------')
def __init__(self, estudiante, id, calificacion):
    self.estudiante = estudiante
    self.id = id
    self.calificacion = calificacion

def obtener_nombre(self):
    return f"Nombre: {self.estudiante}, id: {self.id}, calificacion: {self.calificacion}"

class Estudiante:
    def __init__(self, estudiante, id, calificacion):
        self.estudiante = estudiante
        self.id = id
        self.calificacion = calificacion

    def obtener_nombre(self):
        return f"Nombre: {self.estudiante}, id: {self.id}, calificacion: {self.calificacion}"

    def estudiar(self, horas):
        return f"{self.estudiante} esta estudiando {horas} horas"
    def hacer_tarea(self, horas):
        return f"{self.estudiante} haciendo tarea {horas} horas"
    def entrar_clase(self, bool):
        return f"{self.estudiante} en clase {bool}"

Estudiante1 = Estudiante('Jose', 1, 100)
print(Estudiante1.obtener_nombre())
print(Estudiante1.estudiar(10))
print(Estudiante1.hacer_tarea(5))
print(Estudiante1.entrar_clase(True))
print('------------------')
Estudiante2 = Estudiante('Pepe', 2, 100)
print(Estudiante2.obtener_nombre())
print(Estudiante2.estudiar(10))
print(Estudiante2.hacer_tarea(5))
print(Estudiante2.entrar_clase(True))

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def hacer_sonido(self):
    print('hacer sonido')

def __str__(self):
    return f"Nombre: {self.nombre}, edad: {self.edad}"

class Mascota(Animal):
    def __init__(self, nombre, edad, dueno):
        super().__init__(nombre, edad)
        self.dueno = dueno

class Perro(Mascota):
    def hacer_sonido(self):
        return 'guau'

class Gato(Mascota):
    def hacer_sonido(self):
        return 'miau'

class Vacas(Animal):
    def hacer_sonido(self):
        return 'muu'

def main():
    perro = Perro('perro', 5, 'jose')
    gato = Gato('gato', 2, 'pepe')
    vaca = Vacas('vaca', 10)
    perro.hacer_sonido()
    gato.hacer_sonido()
    vaca.hacer_sonido()
    
    print(f"Nombre: {perro.nombre}, edad: {perro.edad}, dueno: {perro.dueno}")
    print(f"Nombre: {gato.nombre}, edad: {gato.edad}, dueno: {gato.dueno}")
    print(f"Nombre: {vaca.nombre}, edad: {vaca.edad}")



main()

#herencia
#polimorfismo
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def caminar(self):
        print('caminando')

    def __str__(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}, sexo: {self.sexo}"

class estudiantes(Persona):
    def __init__(self, nombre, edad, sexo):
        super().__init__(nombre, edad, sexo)

    def __str__(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}, sexo: {self.sexo}"

class trabajador(Persona):
    def __init__(self, nombre, edad, sexo, salario, trabajo, horario):
        super().__init__(nombre, edad, sexo, salario, trabajo, horario )
        self.salario = salario
        self.trabajo = trabajo
        self.horario = horario

    def __str__(self):
        return f"Nombre: {self.nombre}, edad: {self.edad}, sexo: {self.sexo} salario: {self.salario}, trabajo: {self.trabajo}, horario: {self.horario}"


#polimorfismo
def main():
    persona = Persona('jose', 20, 'masculino')
    estudiante = estudiantes('pepe', 20, 'masculino')
    trabajador = trabajador('jose', 20, 'masculino', 1000, 'programador', '8am a 5pm')
    print(persona)
    print(estudiante)
    print(trabajador)

main()