# 010_a_IntroListFunctionsExtend.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
lista_numeros = [1, 2, 5, 12, 65, 23, 31]
lista_humanos = ["Yamsha", "Goku", "Jesus", "Bush"]

# Se imprime la lista "lista_humanos"
print(lista_humanos)

# Existen muchas funciones para trabajar con listas en python
# Una de ellas es .extend() que se usa para unir "append" otra lista
lista_humanos.extend(lista_numeros)  # A la "lista_humanos" agregale la "lista_numeros"

# Se vuelve a imprimir la "lista_humanos" pero con los elementos de la otra lista agregados.
print(lista_humanos)
