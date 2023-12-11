    # Segunda Clase, Variables & Concatenacion
#-----------------------------------------------------------------------------------------------------#
"""Se recomienda que creemos una variable siempre se escriba con la primera letra en minusculas 
    y si se necesita separar usar _ ejemplo: my_variable o myVariable
    
    NOTA: Las variables de crean una vez que se asigna un valor ejemplo:
                x = 5
                y = "hello, world"
    """


my_variable = "My String variable"
print(my_variable)      


my_variable_int = 100
print(my_variable_int)  # Con esta combinacion lo que se realiza es que se imprima el valor de variable llamada desde print


print(my_variable, my_variable_int) # Este metodo permite concatenar el valor de dos o mas variables llamadas desde la funcion print

#-----------------------------------------------------------------------------------------------------#
    # Ejemplos de Concatenacion

"""
    Para relaizar una concatenacion, se puede hacer uso de variables, para ellos creamos las variables donde se vaya a alojar el valor y solo
    resta imprimir dicho valor en pantalla, para realizarlo en forma de concatenacion (en una sola linea) aplicamos la funsion // 

        print(varible_1, variable_2, variable_3)
"""

    #   Ejemplo Creacion de variables y concatenacion

variable_name = ("Jose Abraham ")
valirble_apellido = ("Escalona Blnaco")
variable_edad = 20
variable_profecion = ("Estudiante de Programacion")

print(variable_name, valirble_apellido, variable_edad, variable_profecion)

#-----------------------------------------------------------------------------------------------------#
# Resultado: Jose Abraham Escalona Blanco 20 Estudiante de Programacion
#-----------------------------------------------------------------------------------------------------#

print("Esta es la edad del usuario Jose:", variable_edad)   # Tambien podemos escribir un mensaje de esta forma y concatenarlo con una variable 

#-----------------------------------------------------------------------------------------------------#
# Resultado: Esta es la edad del usuario Jose: 20
#-----------------------------------------------------------------------------------------------------#

#   Introducir texto en pantalla 

str_name = input ('Indique su Usuario')    # En este caso creamos una variable con el nombre \ str_name \ luego escribimos el texto que queremos que aparezca en pantalla
pin = input ('Ingrese su ID')  # Lo mismo de arriba pero con el PIN

# Esto es para que cuando termine de ingresar las credenciales en pantalla puedan quedar  impresas en la consola 
print(str_name)  
print(pin)


# Forma de crear variables y agregar varchar con saltos de lineas
a = """
Puede asignar una caden 
de varias líneas a una variable 
mediante tres comillas:
"""

print(a)
        
 