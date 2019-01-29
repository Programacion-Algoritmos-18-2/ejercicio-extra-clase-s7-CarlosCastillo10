# Importamos las diferentes clases de los distintos paquetes
from paquete_ordenamiento.modelo import OrdenamientoSeleccion, OrdenamientoInsercion

valores = [4, 2, 5, 3, 1]
valores2 = [4, 2, 5, 3, 1]

ordenSeleccion = OrdenamientoSeleccion(valores)

print("\n%22s\n\n%r\n------------------------\n"%("ARREGLO DESORDENADO",valores))
print("%s\n"%("ORDENAMIENTO POR SELECCION"))
ordenSeleccion.ordenar()

ordenInsercion = OrdenamientoInsercion(valores2)
print("%s\n"%("ORDENAMIENTO POR INSERCION"))
ordenInsercion.ordenar()
