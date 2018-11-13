import Puerto
#Contenedor de nombre y puertos para representar un pais
class Pais:
    def __init__(self,nombre):
        self.nombre = nombre
        self.Puertos = []

    def agregar_puerto(self,nombre,pecesVistos,pecesPescados,coordenadaX,coordenadaY):
        self.Puertos.append(Puerto.Puerto(nombre,pecesVistos,pecesPescados,coordenadaX,coordenadaY))
