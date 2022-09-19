# Tendencias e Innovacion en Tecnologia Agricola (TEA)
# Lecture 09
# Funciones
# Autor: servio@palacios.com
# Fecha: 2022.09.18
# Editado: 2022.09.18
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

# ============================================================
# 1. Utilizando un manejador de archivos
# ============================================================
# x = 2
# x = 4
# print(x)

# ============================================================
# 2. Listas
# ============================================================
# friends = ["Alan", "Michael", "Aura", "Steve"]
# print(friends)

# ============================================================
# 3. Constantes de Listas
# ============================================================
# print([1, 24, 76])
# print(["rojo", "azul", "amarillo"])
# print(["rojo", 10, 9.25])
# print(["rojo", 10, 9.25, [5, 6]])

# ============================================================
# 4. Ya hemos utilizado listas
# ============================================================
# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print("Finalizado!")

# ============================================================
# 5. Listas y Ciclos Definidos
# ============================================================
# friends = ["Alan", "Michael", "Aura", "Steve"]
# for friend in friends:
#     print(friend)
# print("Finalizado!")

# ============================================================
# 6. Buscando en las Listas
# ============================================================
# friends = ["Alan", "Michael", "Aura", "Steve"]
# print(friends[2])

# ============================================================
# 7. Listas son mutables
# ============================================================
# numeros = [4, 7, 1, 63]
# print(numeros)
# numeros[2] = 35
# print(numeros)

# ============================================================
# 8. Longitud de una Lista
# ============================================================
from csv import list_dialects


longitud = len([4, 7, 1, 63])
print(longitud)

# ============================================================
# 9. Usando la función range
# ============================================================
# print(range(4))
# print(len([4, 7, 1, 63]))
# print(range(len([4, 7, 1, 63])))

# ============================================================
# 10. Two loops
# ============================================================
# friends = ["Joseph", "Glenn", "Sally"]

# for friend in friends:
#     print("Happy New Year: ", friend)

# for i in range(len(friends)):
#     print(friends[i])

# ============================================================
# 11. Concatenando Listas
# ============================================================
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
# print(a)

# ============================================================
# 12. Segmentando Listas
# second numnber is up to but not including
# ============================================================
# t = [9, 41, 12, 3, 74, 15]
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[:])

# ============================================================
# 13. Metodos de Listas
# ============================================================
# x = list()
# print(type(x))
# print(dir(x))

# ============================================================
# 14. Creando Listas
# ============================================================
# temporal = list()
# temporal.append("libro")
# temporal.append(99)
# print(temporal)
# temporal.append("galleta")
# print(temporal)

# ============================================================
# 15. Esta algo en la lista?
# ============================================================
# numeros = [1, 9, 21, 10, 16]
# if 9 in numeros:
#     print("El número está en la lista")
# else:
#     print("El número no está en la lista")

# if 15 not in numeros:  # operadores logicos
#     print("El número no está en la lista")
# else:
#     print("El número está en la lista")

# ============================================================
# 16. Orden en Listas
# ============================================================
# friends = ["Joseph", "Glenn", "Sally"]
# friends.sort()
# print(friends)

# ============================================================
# 17. Listas - Funciones predeterminadas
# ============================================================
# numeros = [3, 41, 12, 9, 74, 15]
# print(len(numeros))
# print(max(numeros))
# print(min(numeros))
# print(sum(numeros))
# print(sum(numeros)/len(numeros))

# total = 0
# count = 0
# while True:
#     inp = input('Enter a number: ')
#     if inp == 'done':
#         break
#     value = float(inp)
#     total = total + value
#     count = count + 1

# average = total / count
# print('Average:', average)

# numlist = list()
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average:', average)


# ============================================================
# 18. Listas - Cadenas - Strings
# ============================================================
# cadena = "With three words"
# listaCadenas = cadena.split()
# print(listaCadenas)
# print(len(listaCadenas))
# print(listaCadenas[1])
# for palabra in listaCadenas:
#     print(palabra)

# linea = "primero;segundo;tercero"
# temporal = linea.split()
# print(temporal)
# temporal = linea.split(';')
# print(temporal)

# fhand = open('mbox.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From '):
#         continue
#     words = line.split()
#     print(words[2])
