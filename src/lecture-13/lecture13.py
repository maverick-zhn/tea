# Tendencias e Innovacion en Tecnologia Agricola (TEA)
# Lecture 13
# Listas
# Autor: servio@palacios.com
# Fecha: 2022.10.08
# Editado: 2022.10.08
# =================================================================================
# Disclaimer:
# Este codigo contiene instrucciones de Python que tiene el fin de
# enseñar a programar. De esta forma, los comentarios y contenido puede incluir
# errores de ortografia ya que algunos de estos son simbolos especiales que pueden
# causar algunos problemas al documentar, leer, o utilizar este codigo con
# propositos educativos.
# Best practices: De esta forma se sugiere el uso de estandares de programacion
# que incluyen la reduccion de la utilizacion de Mayusculas o caracteres especiales
# que estan fuera del proposito del programa.
# De forma similar, el código incluye instrucciones que ensenan temas de forma
# progresiva, esto es, puede contener soluciones no optimas.
# =================================================================================


# ============================================================
# 1. Creando un diccionario
# ============================================================
import string
eng2sp = dict()
print(eng2sp)
# # las llaves {} representan el diccionario vacio

# ============================================================
# 2. Agregando elementos a un diccionario
# ============================================================
# eng2sp["one"] = "uno"
# print(eng2sp)

# ============================================================
# 3. Creando un diccionario con valor multiples
# ============================================================
# eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
# print(eng2sp)

# print(eng2sp['two'])

# la siguiente llave/key no existe
# print(eng2sp['noexiste'])


# ============================================================
# 4. len aplicada un diccionario con valor multiples
# ============================================================
# print(len(eng2sp))

# ============================================================
# 5. in aplicada un diccionario con valor multiples
# ============================================================
# buscando keys
# print("one" in eng2sp)
# print("dos" in eng2sp)

# buscando valores
# valores = list(eng2sp.values())
# print("dos" in valores)

# ============================================================
# 6. implementando un contador de letras o caracteres
# histograma
# ============================================================
# palabra = 'brontosaurio'
# d = dict()
# for c in palabra:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] = d[c] + 1

# print(d)

# ============================================================
# 7. utilizando el metodo get en un diccionario
# ============================================================
# cuentas = {'chuck': 1, 'annie': 42, 'jan': 100}
# print(cuentas.get('jan', 0))
# print(cuentas.get('tim', 0))

# ============================================================
# 8. implementando un contador de letras o caracteres
# histograma
# codigo mejorado
# ============================================================
# palabra = 'brontosaurio'
# d = dict()
# for c in palabra:
#     d[c] = d.get(c, 0) + 1
# print(d)


# ============================================================
# 9. diccionarios y archivos
# ============================================================
# fname = input('Ingresa el nombre de archivo: ')
# try:
#     fhand = open(fname)
# except:
#     print('El archivo no se puede abrir:', fname)
#     exit()
# counts = dict()
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)

# ============================================================
# 10. iteradores y diccionarios
# ============================================================
# contadores = {'chuck': 1, 'annie': 42, 'jan': 100}
# for clave in contadores:
#     print(clave, contadores[clave])

# solo los mayores de 10
# contadores = {'chuck': 1, 'annie': 42, 'jan': 100}
# for clave in contadores:
#     if contadores[clave] > 10:
#         print(clave, contadores[clave])

# ============================================================
# 11. imprimiendo la lista ordena de llaves/keys
# ============================================================
# import string
# contadores = {'chuck': 1, 'annie': 42, 'jan': 100}
# lst = list(contadores.keys())
# print(lst)
# lst.sort()
# for clave in lst:
#     print(clave, contadores[clave])

# ============================================================
# 12. analisis de texto avanzado
# elimando signos de puntuacion, admiracion, etc.
# ============================================================
print(string.punctuation)

fname = input('Ingresa el nombre de archivo: ')
try:
    fhand = open(fname)
except:
    print('El archivo no se puede abrir:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
