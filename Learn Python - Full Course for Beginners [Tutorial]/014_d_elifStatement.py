# 014_d_elifStatement.py

# Este script se debe ejecutar varias veces cambiando los valore de las variables
# Primero declaramos 2 variables boolean
# Experimentar con cambiar sus valores a False para ver el resultado
a = False
b = True

# If elif else statement usando not() y and
if a and b:
    print("a y b son True")
# elif permite evaluar de otra manera
elif a and not(b): # not(b) hace que se evalue como lo opuesto
    print("a es True y b es False")
elif not(a) and b:
    print("a es False y b es True")
else:
    print("a y b son False")
