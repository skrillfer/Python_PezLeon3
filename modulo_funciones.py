
import Vista
import Ingresar_Datos.Pantalla1 as Pantalla1
import modulo_agregar
import Estadisticas.View_Estadistica as Vesta

lista_paises = []

#Se inserta informacion_por_defecto a la lista_paises y se agrega a Guatemala 3 Puertos
def informacion_por_defecto():
    modulo_agregar.agregar_pais(lista_paises,'Guatemala')
    modulo_agregar.agregar_pais(lista_paises,'El Salvador')
    modulo_agregar.agregar_pais(lista_paises,'Costa Rica')
    modulo_agregar.agregar_pais(lista_paises,'Panama')
    modulo_agregar.agregar_pais(lista_paises,'Honduras')
    modulo_agregar.agregar_pais(lista_paises,'Nicaragua')
    pais = modulo_agregar.obtener_pais(lista_paises,'Guatemala');
    if not pais==None:
        pais.agregar_puerto('Puerto Barrios',10,33,0.0,0.0)
        pais.agregar_puerto('Puerto San Jose',12,34,0.0,0.0)
        pais.agregar_puerto('Monterrico',200,12,0.0,0.0)
        pais.agregar_puerto('Las Lisas',232,12,0.0,0.0)

#Llama a la funcion mostrar_informacion
def datos_pez_leon():
    mostrar_informacion()

def ingresar_datos():
    Pantalla1.main(lista_paises)

def mostrar_estadisticas():
    Vesta.mostrar(lista_paises)

#Se crea una nueva Ventana llamando a la funcion crear del modulo Vista
def mostrar_informacion():
    Vista.crear(lista_paises)


#-------------------------------------------------------------------------------------
