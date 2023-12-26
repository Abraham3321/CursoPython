


class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def caminar(self):
        print('caminando')

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {self.sexo}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, carrera):
        super().__init__(nombre, edad, sexo)
        self.carrera = carrera

    def caminar(self):
        print('caminando a la escuela')

    def __str__(self):
        return f"{super().__str__()}, Carrera: {self.carrera}"

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, salario, trabajo, horario):
        super().__init__(nombre, edad, sexo)
        self.salario = salario
        self.trabajo = trabajo
        self.horario = horario
    
    def caminar(self):
        print('caminando al trabajo')

    def __str__(self):
        return f"{super().__str__()}, Salario: {self.salario}, Trabajo: {self.trabajo}, Horario: {self.horario}"

# Polimorfismo
def main():
    persona = Persona('José', 20, 'Masculino')
    estudiante = Estudiante('Pepe', 20, 'Masculino', 'Ingeniería')
    trabajador_1 = Trabajador('Juan', 25, 'Masculino', 1500, 'Programador', '9am a 6pm')
    trabajador_2 = Trabajador('Ana', 30, 'Femenino', 2000, 'Diseñador', '10am a 7pm')

    personas = [persona, estudiante, trabajador_1, trabajador_2]

# Ejemplo de polimorfismo
    persona.caminar()  
    print(persona)
    estudiante.caminar()  
    print(estudiante)
    trabajador_1.caminar()  
    print(trabajador_1)
    trabajador_2.caminar()  
    print(trabajador_2)
    print()

main()
