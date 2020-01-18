#Ejercicio01
def descuento(tipo,prestamo):
     # Si el tipo de cliente es EXCLUSIVO
    # Aqui se usa la funcion upper()
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
# Funcion   : Verifica si intNum es un entero
# Parametros: intNum => Numero entero
# Retorna   : bool
def validar_entero(intNum):
    if ( isinstance(intNum, int)):
        return True
    else:
        return False
#fin_validar_entero

#Ejercicio04
# Funcion   : Verifica si fltNum es un real
# Parametros: fltNum => Numero real
# Retorna   : bool
def validar_real(fltNum):
    if ( isinstance(fltNum, float)):
        return True
    else:
        return False

#Ejercicio05
# Funcion   : Devuelve la calificacion del promedio
# Parametros: flotProm ==
# Retorna   : str
def calificacion(fltProm):
    if ( fltProm == 20.0):
        return "Excelente"
    if ( fltProm == 16.0):
        return "Muy Bien "
    if ( fltProm == 12.0):
        return "Regular"
    if ( fltProm == 5.0):
        return "Bajo"
    if ( fltProm == 0.0):
        return "Muy Bajo"
    else:
        return ""
#fin_calificacion

#Ejercicio06
# Funcion   : Devuelve el bonus por puntaje
# Parametros: strCalif == Puntaje
# Retorna   : float
def obtenerBonus(strPuntaje):
    if ( strPuntaje == "Excelente"):
        return 300.0
    if ( strPuntaje=="Muy Bien"):
        return 200.0
    if ( strPuntaje == "Regular"):
        return 100.0
    else:
        return 0.0
#fin_obtenerBonus

#Ejercicio07
def validar_obrero(strObrero):
    #1. El tipo de dato de strObrero es str
    #2. La longitud de la cadena es al menos de 5
    if ( isinstance(strObrero, str) ):
        if ( len(strObrero) >= 5):
            return True     # Es un nombre valido
        else:
            return False    # Insuficients caracteres
    else:
        return False        # No es str
#fin_validar_obrero

#Ejercicio08
def validar_codigo (strCodigo):
    #1. strCodigo es una cadena de 5 caracteres
    #2. El primer caracter de strCodigo es el signo #
    if (len(strCodigo) != 5):
        return False
    if (strCodigo[0] == "#"):
        return True
    #fin_if
#fin_validar_codigo

#Ejercicio09
def validar_anio(intAnio):
    #1.El tipo de dato es intAnio es int
    #2.La longitud del entero es al menos de 2050
    if(isinstance(intAnio,int)):
        if((intAnio) >= 2050):
            return True   #Es anio valido
        else:
            return False
    else:
        return False   #No es int

#Ejercicio10
# Funcion   : Devuelve la calificacion del puntaje
# Parametros: StrPuntaje => Puntaje
# Retorna   : float
def pasa_pedido(strPuntaje):
    if ( strPuntaje == "Excelente"):
        return 100.0
    if ( strPuntaje == "Bajo"):
        return 50.0
    if ( strPuntaje == "Muy bajo"):
        return 20.0
    else:
        return 0.0
#fin_pasa_pedido

#Ejercicio11
# Funcion   : Verifica si intNum es un entero
# Parametros: intNum => Numero entero
# Retorna   : bool
def ganancia(intNum):
    if ( isinstance(intNum, int)):
        return True
    else:
        return False
#fin_ganancia

#Ejercicio12
# Funcion   : Devuelve el puntaje minimo
# Parametros: floatPuntmin ==
# Retorna   : str
def puntaje_minimo(fltPuntmin):
    if ( fltPuntmin == 220.0):
        return "Alcanza puntaje, pase pedido"
    if ( fltPuntmin == 180.0):
        return "Muy bien, le falta poco "
    if ( fltPuntmin == 100.0):
        return "Sigue ofreciendo"
    else:
        return ""
#fin_puntaje_minimo

#Ejercicio13
def validar_empleado(strEmpleado):
    #1. El tipo de dato de strEmpleado es str
    #2. La longitud de la cadena es al menos de 5
    if ( isinstance(strEmpleado, str) ):
        if ( len(strEmpleado) >= 6):
            return True     # Es un nombre valido
        else:
            return False    # Insuficients caracteres
    else:
        return False        # No es str
#fin_validar_empleado

#Ejercicio14
def validar_contrasena (strContrasena):
    #1. strContrasena es una cadena de 5 caracteres
    #2. El primer caracter de strContrasena es el signo #
    if (len(strContrasena) != 5):
        return False
    if (strContrasena[0] == "#"):
        return True
    #fin_if
#fin_validar_contrasena

#Ejercicio15
def es_valido (strNum):
    #1. strNum puede ser un numero de 0-2 o letras de A-C
    if (strNum == "0" or strNum =="1" or strNum =="2" or
        strNum=="A" or strNum =="B" or strNum=="C"):
        return True
    else:
        return False
    #fin_if
#fin_es_valido
