import libreria

#INPUT
nombre=libreria.pedir_nombre("Ingrese nombre:")
tipo=libreria.pedir_entero("Ingrese tipo:", 0, 0)
prestamo=libreria.pedir_real("Ingrese prestamo:")

# PROCESSING
descuento=(libreria * prestamo)


# OUTPUT
libreria.reporte_prestamo(nombre, prestamo, descuento)

