
# Ejercicios creacion de variables y concatenacion

usuario = "Jescalona"
name = "Jose"
apellido = "Escalona"
edad = 20
cargo = "coordinador"

print("Acontinuación presentamos al siguiente personal:", usuario, name, apellido, edad, cargo)

       #   Variables (Asignar varios valores)

"""
    Muchos valores para multibples variables

        Python permite asignar valores a multiples variables en una linea, (esto es para ahorrar lineas de codigo pero tambien se pueden declarar las variables en forma vertical) ejemplo:

        x, y, z = "Orange" , "Banana", "Manzana"

        print(x)
        print(y)
        print(z)
"""

x, y, z = "Orange", "Banana", "Manzana"

print(x)
print(y)
print(z)

"""
    Tambein puede asignar el mismo valor a varias variables en una linea Ejemplo: 

    x = y = z = "Orange"

    print(x)
    print(y)
    print(z) 

    #>>> Orange
    #>>> Orange
    #>>> Orange
"""

x = y = z = "Orange"


print(x)
print(y)
print(z)

    

    #   Desempaquetar una Coleccion

"""
    Si tiene una colecion de valores en una lista, tupa, etc. Python le permite extraer los valores en variables. a esto se le llama desempacar. Ejemplo:

    variableI = ["Carro", "Moto", "Camion"]
    
    x, y, z = variableI

    print(x)
    print(y)
    print(z)

    #>>> Carro
    #>>> Moto
    #>>> Camion
"""

variableI = ["Carro", "Moto", "Camion"]
x, y, z = variableI

print(x)
print(y)
print(z)


    # Variables Globales 

"""
    Caso I 

    Las variables que se crean fuera de una función (como en todos los ejemplos arriba) se conocen como variables globales.
    Las variables globales pueden ser utilizadas por todo el mundo, tanto dentro de funciones y exteriores.

    En este caso creamos una variable dentro de una funcion y se utilizo dentro de una funcion ejemplo:

    x = "hello word"    # Variable

    def variable ():    # Funcion
        print("Llamada a la funcion: " + x)  # Impresion de (msj) + la llamada de la variable "x"
    variable()

    # >>>Llamada a la funcion: hello word
    
"""

x = "Hello Word"

def variable ():
    print("Llamada a la funcion: "+ x)

variable()
    

"""
    Caso II

    Si crea una variable con el mismo nombre dentro de una función, esta variable será local y solo se puede usar dentro de la función. 
    La variable global con el mismo nombre se mantendrá como estaba, global y con el valor original.

    Ejemplo:

    y = "variable_i"    # Variable fuera de la funcion 

    def variable_dentro():
        y = "variable_fuera_ii"     #En este caso se creo una variable dentro de la funcion con el mismo nombre de la variable q esta afuera con la diferencia de q cambia su valor
        print("Llamada de la funcion: " + y)    # Aqui llamamos a la variable "y" que se encuentra dentro de la funcion
    variable_dentro()   # Con esto cerramos la funcion

    print("Llamada de la variable que esta afuera: " + y)   #   Aqui estamos imprimiendo la variable "y" que se encuentra fuera de la funcion


"""

y = "variable_fuera_i"

def variable_dentro():
    y = "variable_ii"
    print("Llamada de la funcion: "+ y)
variable_dentro()

print("Llamada de la funcion que esta afuera:" + y)


    #   La Palabra clave global

"""
    Normalmente, cuando se crea una variable dentro de una funcion, esa variable es local, y solo se puede usar dentro de esa funcion.
    Para crear una variable global dentro de una funcion, puede utilizar la palabra clave. global

    ejemplo:
"""

def variableFuncion():  #   Declaracion de la funcion
    global x    # Palabra clave para globalizar
    x = "variableI" # Valor de la variable
variableFuncion() # Cierre de la funcion

print("Llamada de la funciondentro: " + x)  #Impresion de (msj) + el valor de la variable 



"""
    Caso ii

    Use la palabra clave para cambiar el valor de una variable global dentro de una funcion, consulte la variable mediante el uso de la palabara clave: global

"""

# Creacionde variables e impresion fuera de una funcion  Ejercicios dia 2#  09/12/23

varchar = "Tipo Texto (Str)"
type_int = "Tipo entero (int)"
type_fload = "Tipo decimal (fload)"
type_bool = "Buleano (condiciones)"

print(varchar, type_fload, type_int, type_bool)

print(type(varchar))
print(type(type_int))
print(type(type_bool))
print(type(type_fload))


print("_________________")

varchar_II = "text"
type_fload_II = 5.5
type_bool_II = False
type_int_II = 10


# Con lafuncion type identificamos el tipo de dato de la variable
print(type(varchar_II))
print(type(type_int_II))
print(type(type_bool_II))
print(type(type_fload_II))

print("_____________________")

#   Ejercicios impresion de variable fuera de una funcion

x = "su valor es absoluto es positivo"

def planoCarteciano():
    print("La variable 'X' se tiene en cuenta cuando: " + x)
planoCarteciano()

#>>>La variable 'X' se tiene en cuenta cuando: su valor es absoluto es positivo
print("______________________")


z = "su valor es negativo"
y = "su valor es positivo"

def values():
    print(y, z)
values()

#>>>su valor es negativo su valor es positivo
print("_____________")

x = 120
y = 150

def sustracion():
    print("La sutraccion de: ",  str(y) ,  str(x),   x + y  )
sustracion()

#>>>La sustraccion de: 150 120 270
print("________________")


#   Ejercico 3 operaciones matematicas

x = 10
q = 6
r = 25

print((r * q) // x)
#>>>15
print("_________________")

# Ejercicio 4 operaciones matematicas con variables fuera de una funcion

x = 10
q = 6
r = 25

def operaciones():
    print(x * q * r)
operaciones()

#>>>1500
print("_________________")

# Ejercicio 5 operaciones matematicas con variables fuera de una funcion

q = 6
r = 25
x = 108
def variableF():
    r = 9
    q = 12
    print("Su operacion es: " , r * q)
variableF()

print("El calculo dentro de la funcion dividido entre la variable 'X' es = ", 108 // x)

#variable>>> Su operacion es: 108
#>>> El calculo dentro de la funcion dividido entre la variable 'X' es =  1


#   Ejerccios, formatear un string 10/12/23

"""
    Crea una 4 variables y concatenalas en una Oracion logica con el metodo de formateo #1 (.fromat)
"""
# Ejercicio 1
accion = "salio"
lugar = "casa"
accion_II = "la cola de la gasolina"
insidente = "el carro no ensendia"

print("Juan {} de su {} temprano para poder hacer {} pero {} " .format(accion, lugar, accion_II, insidente))
#>>>Juan salio de su casa temprano para poder hacer la cola de la gasolina pero el carro no ensendia

#Ejercicio 2
x = "asistir"
y = "a una reunion"
z = "martes"
o = "instalacion"
r = "Ysoft Secure"
h = 25
print("Jose debe {} {} el dia, {} para finiquitar la {} de {} el dia {}" .format(x, y, z, o, r, h))
#>>>Jose debe asistir a una reunion el dia, martes para finiquitar la instalacion de Ysoft Secure el dia 25


"""
    Ejercicio con el metodo 2, crear variables y armar oraciones usando el metodo 2 (%) 10/12/23
"""
fecha = 3 
accion = "matenimiento"
equipos = "equipos Versalink"
pauta = "actualizacion"
print("El dia %d se realizo %s a los %s pero quedo pendiente la %s" %(fecha, accion, equipos, pauta))
#El dia 3 se realizo matenimiento a los equipos Versalink pero quedo pendiente la actualizacion