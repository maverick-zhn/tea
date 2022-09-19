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

# Temas
# 1. Utilizando un manejador de archivos
# 2. The Newline caracter
# 8. Maximum and Minimum Loops

# ============================================================
# 1. Utilizando un manejador de archivos
# ============================================================
# fhandle = open("mbox1.txt")
# print(fhandle)

# ============================================================
# 2. The newline caracter
# ============================================================
# mensaje = "Hola,\nMundo!"
# print(mensaje)

# ============================================================
# 3. File handle as a sequence
# ============================================================
# fhandle = open("mbox.txt")
# for linea in fhandle:
#     print(linea)

# ============================================================
# 4. Contando las lineas de un archivo
# ============================================================
# fhandle = open("mbox.txt")
# contador = 0
# for linea in fhandle:
#     contador = contador + 1
#     # print(linea)
# print("Numero de lineas en el archivo ", contador)

# ============================================================
# 5. Leyendo todo el archivo
# ============================================================
# fhandle = open("mbox.txt")
# allFile = fhandle.read()
# print(len(allFile))

# ============================================================
# 6. Buscando en un archivo
# ============================================================
# fhandle = open("mbox.txt")

# for linea in fhandle:
#     if linea.startswith("From:"):
#         print(linea)

# ============================================================
# 7. Buscando en un archivo/fixed
# ============================================================
# fhandle = open("mbox.txt")

# for linea in fhandle:
#     linea = linea.rstrip()
#     if linea.startswith("From:"):
#         print(linea)

# ============================================================
# 8. Saltándose líneas con continue
# ============================================================
# fhandle = open("mbox.txt")

# for linea in fhandle:
#     linea = linea.rstrip()
#     if not linea.startswith("From:"):
#         continue
#     print(linea)

# ============================================================
# 9. Utilizando in para seleccionar líneas
# ============================================================
# fhandle = open("mbox.txt")

# for linea in fhandle:
#     linea = linea.rstrip()
#     if not "@uct.ac.za" in linea:
#         continue
#     print(linea)

# ============================================================
# 10. Preguntando el nombre del archivo
# buenas practicas
# ============================================================
# fileName = input("Ingrese el nombre del archivo: ")
# fhandle = open(fileName)

# for linea in fhandle:
#     linea = linea.rstrip()
#     if not "@uct.ac.za" in linea:
#         continue
#     print(linea)

# ============================================================
# 11. Checkando malos nombres de archivos
# buenas practicas
# ============================================================
fileName = input("Ingrese el nombre del archivo: ")
try:
    fhandle = open(fileName)
except:
    print("El archivo no puede ser abierto: ", fileName)
    quit()

for linea in fhandle:
    linea = linea.rstrip()
    if not "@uct.ac.za" in linea:
        continue
    print(linea)
