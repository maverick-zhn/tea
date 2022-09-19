# Tendencias e Innovacion en Tecnologia Agricola
# Lecture 05
# Ejecución Condicional
# Autor: servio@palacios.com
# Fecha: 2022.09.12
# Editado: 2022.08.12
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
# 1. Operadores Logicos
# 2. Ejecucion Alterna
# 3. Condicionales Encadenados
# 4. Condicionales Anidados
# 5. Exceptiones (try/catch)
# 6. Short-Circuit Evaluation

# ============================================================
# 1. Operadores Logicos
# ============================================================

# 1.1 AND
A = False
B = False
C = A and B
print("Tabla de Verdad para el Operador Logico AND")
print("===========================================")
print("|     A     |       B      |    A and B   |")
print("|-----------------------------------------|")
print("|  ", A, "  |   ", B, "    |   ", C, "    |")
print("|  ", False, "  |   ", True, "     |   ", False and True, "    |")
A = True
B = False
C = A and B
print("|  ", A, "   |   ", B, "    |   ", C, "    |")
A = True
B = True
C = A and B
print("|  ", A, "   |   ", B, "     |   ", C, "     |")
# new line caracter de escape
print("|-----------------------------------------|\n")

# 1.2 OR


# 1.3 NOT
A = not True
B = not False
# print("Tabla de Verdad para el Operador Logico NOT")
# print("Not True es igual a ", A)
# print("Not False es igual a ", B)

# ============================================================
# 1.4 Ejemplo
# Tablas de verdad en acción
# ============================================================
x = 100
y = 100

if not (x > 0 or x < 10):
    print("la condicion es verdadera")
else:
    print("La condicion es falsa")

# ============================================================
# (Libro 3.4) Ejecucion alterna
# ============================================================
# if x >= 0 and x <= 10:
#     print("Es un numero entre 1 y 9")
# else:
#     print("El numero no esta entre 1 y 9")

# if not (x > 0 and x < 10):
#     print("la condicion es verdadera")
# else:
#     print("La condicion es falsa")


# if x > 0:
#     print("x es positivo")
# else:
#     print("x es 0 o negativo")

# ============================================================
# chained conditionals
# ============================================================
# if x < y:
#     print("x es menor que y")
# elif x > y:
#     print("x es mayor que y")
# else:
#     print("x y y son iguales")

# ============================================================
# nested conditionals
# ============================================================
# if x > 0:
#     print("x es positivo")
# else:
#     if x == 0:
#         print("x es 0")
#     else:
#         print("x es negativo")

# ============================================================
# try/except
# https://www.w3schools.com/python/python_try_except.asp
# ============================================================
inp = input("Ingresar la temperatura: ")
# try:
fahrenheit = float(inp)
celcius = (fahrenheit-32) * 5.0/9.0
print("Celcius", celcius)
# except:
print("Please enter a number.")
