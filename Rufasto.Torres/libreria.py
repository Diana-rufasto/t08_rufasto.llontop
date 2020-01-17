#Ejercicio01
def descuento(tipo,prestamo):
    if (tipo.upper()== "COMPULSIVO"):
        return 0.10 * prestamo
    else:
        return 0
def reporte_prestamo(nombre,precio,descuento):
    print("##################################")
    print("#       ficha de boleta          #")
    print("#nombre:              " +nombre+ "")
    print("#precio:       s/. "+str(precio)+"")
    print("#descuento: s/. "+str(descuento)+"")
    print("##################################")






