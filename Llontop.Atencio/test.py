import libreria

assert (libreria.descuento("A", 100) == 0)
assert (libreria.descuento("Excelente", 100) == 10.0)
assert (libreria.descuento("EXCELENTE", 100) == 10.0)
assert (libreria.descuento("ExCeLeNtE", 100) == 10.0)
assert (libreria.descuento("", 100) == 0)
print("descuento OK")


assert (libreria.validar_edad(51) == True)
assert (libreria.validar_edad(55) == True)
assert (libreria.validar_edad(60) == True)
assert (libreria.validar_edad(11) == False)
assert (libreria.validar_edad(19) == False)
print("validar_edad OK")


assert (libreria.validar_mes("") == False)
assert (libreria.validar_mes("MAYO") == False)
assert (libreria.validar_mes("JULIO") == True)
assert (libreria.validar_mes("AGOSTO") == True)
assert (libreria.validar_mes("OCTUBRE") == True)
print("validar_mes OK")


assert (libreria.validar_apellido("") == False)
assert (libreria.validar_apellido("LLONTOP") == True)
assert (libreria.validar_apellido("OLIVA") == False)
assert (libreria.validar_apellido("ATENCIO") == True)
assert (libreria.validar_apellido("AYALA") == False)
print("validar_apellido OK")


assert ((libreria.obtenerDescuento ("FELICIDADES") == 200.0)== True)
assert ((libreria.obtenerDescuento ("MUY BIEN") == 100.0) == True)
assert ((libreria.obtenerDescuento ("FELICICDADES") == 100.0) == False)
assert ((libreria.obtenerDescuento ("MUY BIEN") == 200.0) == False)
assert ((libreria.obtenerDescuento ("FELICIDADES") == 0.0)  ==False)
print("obtenerDescuento OK")



assert (libreria.validar_estacion("") == False)
assert (libreria.validar_estacion("OTOÑO") == False)
assert (libreria.validar_estacion("VERANO") == True)
assert (libreria.validar_estacion("INVIERNO") == True)
assert (libreria.validar_estacion("PRIMAVERA") == True)
print("validar_estacion OK")



assert ((libreria.GanoBoleto ("PERFECTO") == 20.0)== False)
assert ((libreria.GanoBoleto ("LO SENTIMOS") == 10.0)== True)
assert ((libreria.GanoBoleto ("PERFECTO") == 10.0)== False)
assert ((libreria.GanoBoleto ("LO SENTIMOS") == 20.0)== False)
assert ((libreria.GanoBoleto ("") == 20.0)== False)
print("GanoBoleto OK")


assert (libreria.descuento("FELICIDADES", 30.0) == False)
assert (libreria.descuento("FELICIDADES", 15.0) == False)
assert (libreria.descuento("LO SENTIMOS", 30.0) == False)
assert (libreria.descuento("LO SENTIMOS", 15.0) == False)
assert (libreria.descuento("", 30.0) == False)
print("gano jugo OK")


assert ((libreria.GanoBoleto ("FELICIDADES") == 30.0)== False)
assert ((libreria.GanoBoleto ("LO SENTIMOS") == 15.0)== False)
assert ((libreria.GanoBoleto ("FELICIDADES") == 15.0)== False)
assert ((libreria.GanoBoleto ("LO SENTIMOS") == 30.0)== False)
assert ((libreria.GanoBoleto ("") == 30.0)== False)
print("Agotado OK")


assert (libreria.validar_edad(2021) == True)
assert (libreria.validar_edad(2018) == True)
assert (libreria.validar_edad(2009) == True)
assert (libreria.validar_edad(2031) == True)
assert (libreria.validar_edad(2019) == True)
print("validar_anio OK")


assert (libreria.validar_codigo ("ena") == False)
assert (libreria.validar_codigo ("valentina") == False)
assert (libreria.validar_codigo ("VANESA") == False)
assert (libreria.validar_codigo ("dedo") == False)
assert (libreria.validar_codigo ("mesa") == False)
print("validar_codigo OK")


assert ( libreria.validar_ganadero ("PEDRO") == False)
assert ( libreria.validar_ganadero ("ANA") == True)
assert ( libreria.validar_ganadero ("MARIO") == False)
assert ( libreria.validar_ganadero ("SAUL") == True)
assert ( libreria.validar_ganadero ("EMILIO") == False)
print("validar_ganadero ")
