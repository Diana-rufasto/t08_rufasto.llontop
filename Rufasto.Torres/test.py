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

assert (libreria.validar_anio (1990) == False)
assert (libreria.validar_anio (1998) == False)
assert (libreria.validar_anio (2055) == True)
assert (libreria.validar_anio (2067) == True)
assert (libreria.validar_anio (2070) == True)
print("validar_anio OK")

assert ((libreria.pasa_pedido ("Excelente")== 100.0) ==True)
assert ((libreria.pasa_pedido ("Bajo")== 50.0) ==True)
assert ((libreria.pasa_pedido ("Muy bajo")== 20.0) ==True)
assert ((libreria.pasa_pedido ("Excelente")== 800.0) ==False)
assert ((libreria.pasa_pedido ("Excelente")== 560.0) ==False)
print("pasa_pedido OK")

assert (libreria.ganancia("") == False)
assert (libreria.ganancia("#523") == False)
assert (libreria.ganancia(19) == True)
assert (libreria.ganancia(12) == True)
assert (libreria.ganancia(34) == True)
print  ("ganancia OK")

assert ((libreria.puntaje_minimo(220.0) == "Alcanza puntaje, pase pedido") == True )
assert ((libreria.puntaje_minimo(180.0) == "Muy bien, le falta poco ") == True)
assert ((libreria.puntaje_minimo(100.0) == "Sigue ofreciendo") == True)
assert ((libreria.puntaje_minimo(12.0) == "Sigue ofreciendo") == False)
assert ((libreria.puntaje_minimo(50.0) == "Alcanza puntaje, pase pedido") == False)
print ("puntaje_minimo OK")

assert (libreria.validar_empleado ("Enrrique") == True)
assert (libreria.validar_empleado ("Feliciana") == True)
assert (libreria.validar_empleado ("Juan") == False)
assert (libreria.validar_empleado ("Katy") == False)
assert (libreria.validar_empleado ("Niko") == False)
print("validar_empleado OK")

assert (libreria.validar_contrasena ("") == False)
assert (libreria.validar_contrasena ("4324") == False)
assert (libreria.validar_contrasena ("#5256534") == False)
assert (libreria.validar_contrasena ("#174F") == True)
assert (libreria.validar_contrasena ("#1T3R") == True)
print ("validar_contrasena OK")

assert (libreria.es_valido("X") == False)
assert (libreria.es_valido("Z") == False)
assert (libreria.es_valido("A") == True)
assert (libreria.es_valido("B") == True)
assert (libreria.es_valido("C") == True)
print("es_valido OK")
