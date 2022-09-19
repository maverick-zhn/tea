# Tendencias e Innovacion en Tecnologia Agricola (TEA)
# Lecture 06
# Funciones
# Autor: servio@palacios.com
# Fecha: 2022.09.10
# Editado: 2022.08.10
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
# 1. Built-in functions
# 2. Funciones de Conversion de Tipos
# 3. Funciones Matematicas
# 4. Numeros Aleatorios
# 5. Agregando Nuevas Funciones

# ============================================================
# 1. Funciones built-in
# ============================================================
# mensaje = "Hola, Mundo!"
# longitud = len(mensaje)
# print(longitud)

# ============================================================
# 2. Funciones de Conversion de Tipos
# ============================================================
# 2.1 int()
# horas = input("horas trabajadas? ")
# valorPorHora = input("valor por hora? ")

# se utiliza la conversion de tipo a int
# sino se hace la conversion existira error porque trata de multiplicar strings
# total = int(horas) * int(valorPorHora)
# print(total)

# 2.2 float()
# fahrenheit = float(32)
# print(fahrenheit)
# print(type(fahrenheit))

# pi = float("3.14159654")
# print(pi)
# print(type(pi))

# 2.3 str()
# strTemperatura = str(32)
# print(strTemperatura)
# print(type(strTemperatura))

# print(type(str(3.141592654)))

# ============================================================
# 3.0 Funciones Matematicas
# https://docs.python.org/3/library/math.html
# ============================================================
# print("================ Funciones Matematicas =================")
# print(math)

# radians = 0.7
# height = math.sin(radians)
# print(height)
# print(type(height))

# degrees = 45

# # raiz cuadrada
# print(math.sqrt(144))

# ============================================================
# 4.0 Numeros Aleatorios
# https://docs.python.org/3/library/random.html
# ============================================================
# El laboratorio contendra un ejercicio similar al siguiente
# print("================ Numeros Aleatorios =================")
# for i in range(10):
#     aleatorio = random.random()
#     print(aleatorio)

# print(random.randint(5, 10))

# valores = [1, 2, 3, 4, 5]
# aleatorio = random.choice(valores)
# print(aleatorio)

# ============================================================
# 5.0 Agregando Nuevas Funciones
# https://realpython.com/defining-your-own-python-function/
# ============================================================


def fahrenheit2Celcius(pCelcius):
    temperatureFahrenheit = (9/5) * pCelcius + 32
    print(temperatureFahrenheit)


try:
    temperaturaCelcius = float(input("Cual es la temperatura en Celcius? "))
except:
    print("Introducir un numero.")

fahrenheit2Celcius(temperaturaCelcius)
