# Tendencias e Innovacion en Tecnologia Agricola (TEA)
# Lecture 07
# Funciones
# Autor: servio@palacios.com
# Fecha: 2022.09.17
# Editado: 2022.08.17
# =================================================================================
# Disclaimer:
# Este codigo contiene instrucciones de Python que tiene el fin de
# enseñar a programar. De esta forma, los comentarios y contenido puede incluir
# errores de ortografia ya que algunos de estos son simbolos especiales que pueden
# causar algunos problemas al documentar, leer, o utilizar este codigo con
# propósitos educativos.
# Best practices: De esta forma se sugiere el uso de estandares de programacion
# que incluyen la reduccion de la utilizacion de Mayusculas o caracteres especiales
# que estan fuera del proposito del programa.
# De forma similar, el código incluye instrucciones que ensenan temas de forma
# progresiva, esto es, puede contener soluciones no optimas.
# =================================================================================

# Temas
# 1. Recuperando caracterres de la cadena por medio de
# 2. Iteracion sobre cadenas
# 8. Maximum and Minimum Loops

# ============================================================
# 1. Recuperando caracterres de la cadena por medio de
#    indices
# ============================================================
#   0   1   2   3   4   5   6   7   8   9   10  11
# | H | o | l | a | , |   | M | u | n | d | o | ! |
mensaje = "Hola, Mundo!"
# caracter = mensaje[3]
# print(caracter)
# caracter = mensaje[7]
# print(caracter)


# ============================================================
# 2. Iteracion sobre cadenas
# ============================================================
# index = 0
# while index < len(mensaje):  # probar con <=
#     caracter = mensaje[index]
#     print(caracter)
#     index = index + 1

# for i in range(len(mensaje)):
#     print(mensaje[i])

# for caracter in mensaje:
#     print(caracter)

# ============================================================
# 3. String Slices (Secciones/Segmento de Cadenas)
# ============================================================
#   0   1   2   3   4   5   6   7   8   9   10  11
# | M | o | n | t | y | _ | P | y | t | h | o | n |
s = "Monty_Python"

# El operador retorna la parte del string empezando de la
# posicion n hasta la posicion m sin incluir el indice m
# print(s[0:6])

# print(s[6:12])

# Si se omite el primer índice, el operador empieza desde 0
# print(s[:5])

# Si se omite el segundo índice, el operador llega hasta el
# final
# print(s[6:])

# ============================================================
# 4. Ciclos y Contadores
# ============================================================
# contador = 0
# for caracter in mensaje:
#     if caracter == 'o':
#         contador = contador + 1
# print("Total de o(s) en el mensaje: ", contador)

# ============================================================
# 5. Operador in
# ============================================================
# if 'a' in mensaje:
#     print("El string contiene a(s)")


# ============================================================
# 6. Comparacion de Strings
# ============================================================
# if "Hola, Mundo!" != mensaje:
#     print("Los dos strings(textos) no son iguales")
# else:
#     print("Los dos strings(textos) son iguales")

# adicionalmente, se puede utilizar el operador < y > para
# ordenar alfabeticamente un texto

# ============================================================
# 7. Métodos de Strings
# Python object: contains data and methods (built-in functions)
# https://www.w3schools.com/python/python_ref_string.asp
# ============================================================
# print(dir(mensaje))

# pasando todo a mayuscula
# mensajeMayuscula = mensaje.upper()  # invocando el método
# print(mensajeMayuscula)

# pasando todo a minuscula
# mensajeMinucula = mensaje.lower()
# print(mensajeMinucula)

# buscando caracteres en el string
# index = mensaje.find("!")
# print(index)

# probar algunos métodos de los strings

# remover espacios (white space)
# linea = "   este texto tiene espacios     "
# print(linea)
# print(linea.strip())

# linea = "Que tenga feliz dia"
# print(linea.startswith("Que"))

# print(linea.lower().startswith("Que"))

# ============================================================
# 8. Analizando cadenas
# Análisis de datos
# Parsing Strings
# ============================================================

# dato = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# arrobapos = dato.find('@')
# print(arrobapos)

# espos = dato.find(' ', arrobapos)
# print(espos)

# direccion = dato[arrobapos+1:espos]
# print(direccion)

def thing():
    print("Hello")


# print("There")

# x = 'banana'
# y = max(x)
# print(y)


# def func(x):
#     print(x)


# func(10)
# func(20)


# def stuff():
#     print('Hello')
#     return
#     print('World')


# stuff()


# def greet(lang):
#     if lang == 'es':
#         return 'Hola'
#     elif lang == 'fr':
#         return 'Bonjour'
#     else:
#         return 'Hello'


# print(greet('fr'), 'Michael')


def addtwo(a, b):
    added = a + b
    return a


x = addtwo(2, 7)
print(x)
