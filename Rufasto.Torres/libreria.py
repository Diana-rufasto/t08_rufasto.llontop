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

#Ejercicio02
def validar_nombre(strNombre):
    #1. El tipo de dato de strNombre es str
    #2. La longitud de la cadena es al menos de 3
    if ( isinstance(strNombre, str) ):
        if ( len(strNombre) >= 3):
            return True     # Es un nombre valido
        else:
            return False    # Insuficients caracteres
    else:
        return False        # No es str
#fin_validar_nombre

#Ejercicio03
def validar_entero(intNum):
    if ( isinstance(intNum, int)):
        return True
    else:
        return False
#fin_validar_numero

