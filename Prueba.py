class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Correo: {self.correo}")

    def validar_correo(self, dominio):

        while not self.correo.endswith(dominio):
            print("Ingrese un dominio válido.")

            self.nombre = input("Ingrese su nombre: ")
            self.apellido = input("Ingrese su apellido: ")
            self.correo = input("Ingrese su correo: ")

        self.mostrar_informacion()


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
correo = input("Ingrese su correo: ")

usuario1 = Usuario(nombre, apellido, correo)
usuario1.validar_correo("@utb.edu.co")
