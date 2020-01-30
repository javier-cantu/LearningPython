# 010_i_IntroListFunctionsReverse.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
lista_numeros = [1, 2, 5, 12, 65, 23, 31]
lista_humanos = ["Yamsha", "Goku", "Goku", "Goku", "Jesus", "Bush"]

# Se imprimen las listas en el orden original
print(lista_humanos)
print(lista_numeros)

# Existen muchas funciones para trabajar con listas en python
# Una de ellas es .reverse() que se usa para invertir el orden de los elementos de la lista
# Primero se invierten los elementos con reverse()
lista_humanos.reverse()
lista_numeros.reverse()

# Luego las mandamos imprimir invertidas.
print(lista_humanos)  # ['Bush', 'Jesus', 'Goku', 'Goku', 'Goku', 'Yamsha']
print(lista_numeros)  # [31, 23, 65, 12, 5, 2, 1]
