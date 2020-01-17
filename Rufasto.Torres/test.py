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
