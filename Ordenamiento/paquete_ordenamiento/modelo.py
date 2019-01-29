# Clase Ordenamiento Por Seleccion
class OrdenamientoSeleccion(object):

	# Constructor
	def __init__(self, valores):
		self.agregar_datos(valores)
	
	def agregar_datos(self, valores):
		self.datos = valores

	def obtener_datos(self):
		return self.datos

	def __str__(self):
		temporal = ""

		for elemento in self.obtener_datos():
			temporal = ("{0} {1} ".format(temporal, elemento))

		temporal = ("{0}{1}".format(temporal, "\n"))
		return temporal
	
	# Metodos de agregar
	
	def ordenar(self):

		for x in range(0,len(self.obtener_datos()) - 1):
			masPequenio = x;
		
			for indice in range( x + 1, len(self.obtener_datos())):
				if(self.obtener_datos()[indice] < self.obtener_datos()[masPequenio]):
					masPequenio = indice

			self.intercambiar(x, masPequenio)

			print(self.__str__())


	def intercambiar(self, primero, segundo):
		temporal = self.obtener_datos()[primero]
		self.obtener_datos()[primero] = self.obtener_datos()[segundo]
		self.obtener_datos()[segundo] = temporal

# Clase Ordenamiento Por Insercion
class OrdenamientoInsercion(object):

	# Constructor
	def __init__(self, valores):
		self.agregar_datos(valores)
	
	def agregar_datos(self, valores):
		self.datos = valores

	def obtener_datos(self):
		return self.datos

	def __str__(self):
		
		temporal = ""

		for elemento in self.obtener_datos():
			temporal = ("{0} {1} ".format(temporal, elemento))

		temporal = ("{0}{1}".format(temporal, "\n"))
		return temporal

	def ordenar(self):

		for siguiente in range(1, len(self.obtener_datos())):
			
			insercion = self.obtener_datos()[siguiente]
			moverElemento = siguiente

			while(moverElemento > 0 and self.obtener_datos()[moverElemento -1] > insercion):
				self.obtener_datos()[moverElemento] = self.obtener_datos()[moverElemento - 1]
				moverElemento = moverElemento - 1;

			self.obtener_datos()[moverElemento] = insercion

			print(self.__str__())