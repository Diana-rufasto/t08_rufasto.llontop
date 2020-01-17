import libreria

#INPUT
nombre=libreria.pedir_nombre("ingrese nombre:")
tipo=libreria.pedir_entero("ingrese tipo:",0,0)
prestamo=libreria.pedir_real("ingrese prestamo:")

# PROCESSING
descuento=(libreria*prestamo)

# OUTPUT
libreria.reporte_prestamo(nombre,prestamo,descuento)
