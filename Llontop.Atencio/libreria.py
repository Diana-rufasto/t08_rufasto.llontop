#ejercicio1

def descuento(tipo, prestamo):
    # Si el tipo de cliente es EXCELENTE
    # Aqui se usa la funcion upper()
    if ( tipo.upper() == "EXCELENTE" ):
        return 0.10 * prestamo
    else:
        return 0

def reporte_prestamo(cliente, monto,descuento):
    print("########################")
    print("# REPORTE DE PRESTAMO #")
    print("# Nombre:"  ""+ nombre+"")
    print("# Precio: S/." "+ str(precio)+")
    print("# Descuento: S/." + str(descuento)+"")
    print("#########################")

#fin_descuento

#ejercicio2
def validar_edad(intEdad):
    #1.El tipo de dato es intEdad es int
    #2.La longitud del entero es al menos de 50
    if (isinstance(intEdad,int)):
        if((intEdad) >= 50):
            return True   #Es edad valido
        else:
            return False  #Insuficiencia caracteres
    else:
        return False   #No es int
#fin_validar_edad


#ejercicio3
def validar_mes(strMes):
    #El tipo de dato es strMes es str
    #La longitud de la cadena es al menos 5
    if (isinstance(strMes,str)):
        if(len(strMes) >=5):
            return True     #Es un mes valido
        else:
            return False    #Insuficiente caracteres
    else:
        return False       #No es str
#fin_validar_mes


#ejercicio4
def validar_apellido(strApellido):
    #El tipo de dato es strApellido es str
    #La longitud de de la cadena es al menos 6
    if (isinstance(strApellido,str)):
        if (len(strApellido) >= 6):
            return True     #Es un apellido valido
        else:
            return False    #Insuficiente caracteres
    else:
        return False        #No es str
#fin_validar_apellido


#ejercicio5
# Funcion   : Devuelve el bono por calificacion
# Parametros: strCalif => Calificacion
# Retorna   : float
def obtenerDescuento(strCalif):
    if ( strCalif == "FELICIDADES"):
        return 200.0
    if ( strCalif == "MUY BIEN"):
        return  100.0
    else:
        return 0.0
#fin_obtenerDescuento


#ejercicio6
def validar_estacion(strEstacion):
    #El tipo de dato es strMes es str
    #La longitud de la cadena es al menos 6
    if (isinstance(strEstacion,str)):
        if(len(strEstacion) >=6):
            return True     #Es un mes valido
        else:
            return False    #Insuficiente caracteres
    else:
        return False       #No es str
#fin_validar_mes


# Funcion   : Devuelve el bono por calificacion
# Parametros: strCalif => Calificacion
# Retorna   : float
def GanoBoleto(strCalif):
    if ( strCalif == "PERFECTO!"):
        return 20.0
    if ( strCalif == "LO SENTIMOS"):
        return  10.0
    else:
        return 0.0
#fin_obtenerDescuento


#ejercicio8
def descuento(tipo, prestamo):
    # Si el tipo de cliente es EXCELENTE
    # Aqui se usa la funcion upper()
    if ( tipo.upper() == "EXCELENTE" ):
        return 0.10 * prestamo
    else:
        return 0

def reporte_prestamo(cliente, monto,descuento):
    print("########################")
    print("# REPORTE DE PRESTAMO #")
    print("# Nombre:"  ""+ nombre+"")
    print("# Precio: S/." "+ str(precio)+")
    print("# Descuento: S/." + str(descuento)+"")
    print("#########################")


#ejercicio9
def Gano_jugo(strPromedio):
    if ( strPromedio == "FELICIDADES"):
        return 30.0
    if ( strPromedio == "LO SENTIMOS"):
        return  15.0
    else:
        return 0.0
#fin_agotado


#ejercicio10
def validar_anio(intAnio):
    #1.El tipo de dato es intAnio es int
    #2.La longitud del entero es al menos de 2020
    if (isinstance(intAnio,int)):
        if((intAnio) >= 2020):
            return True   #Es anio valido
        else:
            return False  #Insuficiencia caracteres
    else:
        return False   #No es int
#fin_validar_anio


#ejercicio11
def validar_codigo(strCodigo):
    #1.strCodigo es una cadena de 6 caracteres
    #2.El primer caracter de strCodigo es el signo #
    if (len(strCodigo)!=6):
        return False
    if(strCodigo[0]=="#"):
        return True
    #fin_if
#fin_validar_codigo


#ejercicio12
def validar_ganadero(strGanadero):
    #1.El tipo de dato es strGanadero es str
    #2.L alongitud de la cadenaes al menos de 4
    if (isinstance(strGanadero,str)):
        if (len(strGanadero)>=4):
            return True    #es u nombre valido
        else:
            return False   #insuficiente caracrteres
    else:
        return False       #No es str
#fin_validar_ganadero
