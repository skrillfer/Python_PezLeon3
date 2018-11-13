import Pais

#se agrega un pains a la lista de paises
def agregar_pais(lista_paises,nombre):
    lista_paises.append(Pais.Pais(nombre));

#Se recorre la lista de paises para verificar si coincide con 'nombre'
#Retorna Verdadero o Falso
def existe_pais(lista_paises,nombre):
    for pais in lista_paises:
        if pais.nombre.lower() == nombre.lower():
            return True
    return False

#Se recorre la lista de puertos que contiene el pais, para verificar si coincide con 'nombre'
#Retorna Verdadero o Falso
def existe_puerto(Pais,nombre):
    for port in Pais.Puertos:
        if port.nombre.lower() == nombre.lower():
            return True
    return False

#se obtiene un pais recorriendo la lista de paises y al encontrar una coincidencia con nombre_pais entonces se retorna
#Retorna un Pais o None
def obtener_pais(lista_paises,nombre_pais):
    for pais in lista_paises:
        if pais.nombre.lower()==nombre_pais.lower():
            return pais
    return None
