#    Cadenas de Comprobacion 11/12/23

"""

    Para comprobar si una determinada frase o carácter está presente en una cadena, podemos usar La palabra clave (in)
"""
#Ejercicio 01
v_txt = "Comprobacion de variables"
print("variable" in v_txt)
#>>>True

"""
    .if Úsalo en una declaración:if

    En este caso le decimos a la funcion que si la palabra "valor" esta alojada en la variable "txt"
    se imprima el mensaje "si, el valor esta presente"
"""
# Imprima solo si "valor" está presente:
#Ejercicio #02
txt = "Comprobacion de valor"
if "valor" in txt:
    print("si, el valor esta presente")
    #>>>si, el valor esta presente

print("______________________________")

"""
    .not in  Para comprobar si una determinada frase o carácter NO está presente en una cadena, 
    podemos usar La palabra clave .not in
"""
#Comprueba si "db" NO esta presente en el texto
#Ejercicio 03
v_not = "Mysql es un motor db"
print("db" not in v_not)
#>>>False 
print("_________________________")

"""
    if  Úsalo en una declaración: if
"""
# Imprima solo si "db" NO esta presente:
#Ejercicio 04
txt_v = "Comprobacion del valor db"
if "dr" not in txt_v:
    print("El valor (db) no esta en la variable declarada")
    #>>>El valor (db) no esta en la variable declarada
