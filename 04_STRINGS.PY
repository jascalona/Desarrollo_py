    # Cuarta Clase, STRINGS

variable_salto_linea = "Con esta funcion barra invertida y 'n' podemos realizar\nun salto de linea al momento de imprimir en panatalla"
print(variable_salto_linea)
# Con la funcion (\n) podemo realizar un salto de linea

variable_tab = "\tCon esta funcion barra invertida 't' podemos realizar una tabulacion al momento de imprimir en panatalla"
print(variable_tab)
# Con la funcion (\t) podemos realizar una tabulacion

var = 20
intt = 10
print("\tProbando tabulacion con enteros es = ", var * intt)
# Si solo hay tipos de datos enteros no se puede realizar la tabulacion


var = 20
r = 20
print(str(var) + " " + str(r))
# En este caso se procedio a convertir convertir los datos de type int a str pero no es compatible con barras invertida
#>>>20 20


"""
   Concepto #2  --formatear un string (esto es para poder ir agregando textos y los valores de las variables)

   existen dos formas la primera es utilizando el "{}"  y al final el  .format(variable_1, varibale_2, variable_3)
"""


name = "Jose"
surname = "Escalona"
age = 20
 
print("my name is {} my surname {} age {} " .format(name, surname, age))
#>>> my name is Jose my surname is Escalona age 20

"""
De esta forma podemos ir combinando cadenas de textos impresas con datos de variables
Esto es tipico para cuando se intercionaliza texto en otros idiomas (esto es una forma de concatenar cuando se usan variables y texto)
"""

# Ejemplo de como no se debe hacer 


name = "Jose"
surname ="Escalona"
age = 20

print("my name is" + " " + name + " " "my surname is" " " + surname + " " + "my age is" + " " + str(age))
# Concatenar datos de esta forma es mas largo y al interprete le cuesta ejecutar


# Ejercicio concatenaciones str

name = "Anais"
surname = "Lucena"
age = 21
Condicion = "Se come los mocos"

print("Ella se llama {} Se apellida {} Tiene {} A;os {} Pero es muy boninta" .format(name, surname, age, Condicion))
#>>>Ella se llama Anais Se apellida Lucena Tiene 21 A;os Se come los mocos Pero es muy boninta

#------------------------------------------------------------------------------------------------------------------

""" Otra forma de concatenar y hacer el programa mas seguro es implementando los %s y %d y al final usar  %(variable_1, variable_2, variable_3)

 %s = para str
 %d = para int

"""

coloresPrimarios = "rojo", "amarillo", "verde" 
coloresSecundarios = "morado", "azul", "negro"

print("Para relaizar un cuadro es importante tener encuneta los colores primario los cuales son %s luego para definir podemos usar los colores %s "  %(coloresPrimarios, coloresSecundarios))
#>>>Para relaizar un cuadro es importante tener encuneta los colores primario los cuales son ('rojo', 'amarillo', 'verde') luego para definir podemos usar los colores ('morado', 'azul', 'negro')
  
# Ejercicio con int

coloresPrimarios = 3
coloresSecundarios = 4

print("Los colores son muchos pero para esta prueba solo vamos a usar los colores primarios los cuales son %d y los colores secundarios los cuales son %d " %(coloresPrimarios, coloresSecundarios))
#>>>Los colores son muchos pero para esta prueba solo vamos a usar los colores primarios los cuales son 3 y los colores secundarios los cuales son 4

"""
    Cabe destacar que de esta forma la ejecucion es mas precisa que con el {} .format ya que si con los % se coloca un valor cuyo caracter no corresponde a al type especificado ya sea (str o int) mostrara error
    Ejemplo

coloresSecundarios = 10
coloresPrimarios = "nueve"
print("Los colores secundarios son %d y los colores primarios son %s " %(coloresSecundarios, coloresPrimarios))

"""

# Funciones del sistema

"""
Lista:

capitalize: coloca la primera letra en mayuscula
lower: coloca todas las letras en minusculas
upper: coloca todas las letras en mayusculas
count(" "): cuenta cuantas letras hay, esto lo especificamos colocando la letra en ejemplo ("t") 
isnumeric: Con esta funcion podemos decirle al sistema q nos identifique si un valor es numerico, si es es numerico dira true y si no dira false
startswith: se usa para saber si un valor empieza con algun dato en especifico ejemplo ("py") si es verdad dira true y asi sucesivamente

"""

lenguaje = "python"

print(lenguaje.capitalize())

print(lenguaje.upper())

print(lenguaje.count("t"))

print(lenguaje.isnumeric())

print(lenguaje.lower())

print(lenguaje.startswith("py"))

print("______________________________")
# Bucle a través de una cadena 11/12/23

"""
Cuando escribe código, a menudo necesita encontrar una manera de repetir algo,
 por eso es necesario utilizar los bucles en python. Es posible que deba iterar sobre caracteres en una cadena u objetos en una cadena. 
 List es el proceso de iterar sobre algo que se realiza a través de un bucle.

    Python tiene dos construcciones de bucle:

    * Bucle for 
    * Bucle while

En lugar de iterar sobre una secuencia, puede usar un bucle para hacer lo mismo varias veces. Un ejemplo es un servidor web,
que es esencialmente un bucle infinito. El servidor escucha y espera a que el cliente envíe un mensaje. 
Cuando se recibe el mensaje, el bucle llama a la función en consecuencia.

Otro ejemplo es un bucle de juego: ganar o perder un juego generalmente no termina el juego. 
En su lugar, se le preguntará si desea volver a jugar. Esto también se puede hacer envolviendo todo el programa en un bucle.    
    
"""
# Ejemplo, en este caso podemos ver como se deglosa el contenido

pip_list = 1,2,3

for item in pip_list:
    print(item)

#   Estduar Bucles  11/12/23


