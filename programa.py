class Persona:
    def __init__(self, nombre, edad, sexo):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
    
    def _caminar(self):
        print('caminando')

    def __str__(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Sexo: {self._sexo}"

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, carrera):
        super().__init__(nombre, edad, sexo)
        self._carrera = carrera

    def _caminar(self):
        print('caminando a la escuela')

    def __str__(self):
        return f"{super().__str__()}, Carrera: {self._carrera}"

class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, salario, trabajo, horario):
        super().__init__(nombre, edad, sexo)
        self._salario = salario
        self._trabajo = trabajo
        self._horario = horario
    
    def _caminar(self):
        print('caminando al trabajo')

    def __str__(self):
        return f"{super().__str__()}, Salario: {self._salario}, Trabajo: {self._trabajo}, Horario: {self._horario}"

# Polimorfismo
def main():
    persona = Persona('José', 20, 'Masculino')
    estudiante = Estudiante('Pepe', 20, 'Masculino', 'Ingeniería')
    trabajador_1 = Trabajador('Juan', 25, 'Masculino', 1500, 'Programador', '9am a 6pm')
    trabajador_2 = Trabajador('Ana', 30, 'Femenino', 2000, 'Diseñador', '10am a 7pm')

    personas = [persona, estudiante, trabajador_1, trabajador_2]

    # Ejemplo de polimorfismo
    persona._caminar()  
    print(persona)
    estudiante._caminar()  
    print(estudiante)
    trabajador_1._caminar()  
    print(trabajador_1)
    trabajador_2._caminar()  
    print(trabajador_2)
    print()

main()
