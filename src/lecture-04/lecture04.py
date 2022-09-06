# source code
# correctness
# design
# style
# cli = command line interface
# gui = graphical user interface
# best practices (lower case)

x = -1
y = 10

# if x > 0:
#     print("x es positivo")
# else:
#     print("x es 0 o negativo")

# chained conditionals
# if x < y:
#     print("x es menor que y")
# elif x > y:
#     print("x es mayor que y")
# else:
#     print("x y y son iguales")


# nested conditionals
if x > 0:
    print("x es positivo")
else:
    if x == 0:
        print("x es 0")
    else:
        print("x es negativo")
