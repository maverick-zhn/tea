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
import math
import random

# Temas
# 1. Actualizando Variables que dependen de un valor anterior
# 2. While (Mientras)
# 3. Iteración Infinita
# 4. Continue
# 5. for
# 6. Loop patterns
# 7. Contando y Sumando en Loops (iteración/ciclos)
# 8. Maximum and Minimum Loops

# ============================================================
# 1. Actualizando Variables que dependen de un valor anterior
# ============================================================
x = 0

x = x + 1

print(x)

# ============================================================
# 2. While (Mientras)
# ============================================================
# deje bug
# evalua la condicion
# si verdadero ejecuta el cuerpo del ciclo
# si la condicion es falsa, entonces se ejecuta la siguiente
# linea despues del ciclo
n = 5
while n > 5:
    print(n)
    n = n - 1

print("Autodestruir!")
# ============================================================
# 3. Iteracion Infinita
# ============================================================
# n = 10
# while True:
#     print(n, end=' ')
#     n = n - 1
# print("Finalizado!")

# while True:
#     line = input("> ")
#     if line == "done":
#         break
#     print(line)
# print("Finalizado!")

# ============================================================
# 4. Continue, break
# ============================================================
# while True:
#     line = input("> ")
#     if line[0] == '#':
#         continue
#     if line == "done":
#         break
#     print(line)
# print("Finalizado!")

# ============================================================
# 5. for
# ============================================================
# friends = ["steve", "alan", "michael", "erdos"]

# for friend in friends:
#     print("Feliz año nuevo: ", friend)
# print("Finalizado")

# ============================================================
# 6. Loop patterns
# ============================================================
# ============================================================
# 7. Contando y Sumando en Loops (iteración/ciclos)
# ============================================================
# 7.1 Contando elementos
# contador = 0

# for i in [3, 41, 12, 9, 74, 15]:
#     contador = contador + 1

#print("Número de elementos: ", contador)

# 7.2 Sumando elementos
# total = 0

# for i in [3, 41, 12, 9, 74, 15]:
#     total = total + i

# print("Total de la suma: ", total)


# ============================================================
# 8. Maximum and Minimum Loops
# ============================================================
# None = https://www.w3schools.com/python/ref_keyword_none.asp
largest = None
print("Antes: ", largest)
for i in [3, 41, 12, 9, 74, 15]:
    if largest is None or i > largest:
        largest = i
    print("Loop: ", i, largest)
print(largest)


def max(values):
    largest = None
    #print("Antes: ", largest)
    for i in values:
        if largest is None or i > largest:
            largest = i
        #print("Loop: ", i, largest)
    return largest


print("El valor más grande en la lista es: ", max([3, 41, 12, 9, 74, 15]))
