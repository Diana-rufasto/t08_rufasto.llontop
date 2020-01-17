import libreria

assert (libreria.descuento("A", 100) == 0)
assert (libreria.descuento("Compulsivo", 100) == 10.0)
assert (libreria.descuento("COMPULSIVO", 100) == 10.0)
assert (libreria.descuento("CoMpUlSiVo", 100) == 10.0)
assert (libreria.descuento("", 100) == 0)
print("descuento OK")

assert (libreria.validar_nombre("") == False)
assert (libreria.validar_nombre("ES") == False)
assert (libreria.validar_nombre("Diana") == True)
assert (libreria.validar_nombre("Ana") == True)
assert (libreria.validar_nombre("Maria") == True)
print ("validar_nombre OK")

assert (libreria.validar_entero("") == False)
assert (libreria.validar_entero("#123") == False)
assert (libreria.validar_entero(12) == True)
assert (libreria.validar_entero(29) == True)
assert (libreria.validar_entero(54) == True)
print  ("validar_entero OK")

assert  (libreria.validar_real("")== False)
assert  (libreria.validar_real("12")== False)
assert  (libreria.validar_real(12.90)== True)
assert  (libreria.validar_real(34.21)== True)
assert  (libreria.validar_real(56.34)== True)
print  ("validar_real OK")

assert ((libreria.calificacion(20.0) == "Excelente") == True )
assert ((libreria.calificacion(16.0) == "Muy Bien") == False)
assert ((libreria.calificacion(20.0) == "Muy Bien") == False)
assert ((libreria.calificacion(12.0) == "Regular") == True)
assert ((libreria.calificacion(5.0) == "Bajo") == True)
print ("calificacion OK")

assert ((libreria.obtenerBonus("Excelente") == 300.0) == True)
assert ((libreria.obtenerBonus("Excelente") == 200.0) == False)
assert ((libreria.obtenerBonus("Muy Bien") == 200.0) == True)
assert ((libreria.obtenerBonus("Regular") == 300.0) == False)
assert ((libreria.obtenerBonus("Regular") == 100.0) == True)
print ("obtener_bonus OK")

assert (libreria.validar_obrero ("Ernesto") == True)
assert (libreria.validar_obrero ("Yennifer") == True)
assert (libreria.validar_obrero ("Ana") == False)
assert (libreria.validar_obrero ("Eli") == False)
assert (libreria.validar_obrero ("Alex") == False)
print("validar_obrero OK")

assert (libreria.validar_codigo ("") == False)
assert (libreria.validar_codigo ("1234") == False)
assert (libreria.validar_codigo ("#125134") == False)
assert (libreria.validar_codigo ("#151F") == True)
assert (libreria.validar_codigo ("#123R") == True)
print ("validar_codigo OK")


