#Clase puerto, se definen sus variables nombre,pecesVistos,pecesPescados,coordenadaX,coordenadaY,profundidades_visto
class Puerto:
    def __init__(self,nombre,pecesVistos,pecesPescados,coordenadaX,coordenadaY):
        self.nombre = nombre
        self.pecesVistos = pecesVistos
        self.pecesPescados = pecesPescados
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.profundidades_visto = []
