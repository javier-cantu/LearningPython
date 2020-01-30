# 010_f_IntroListFunctionsPop.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
lista_numeros = [1, 2, 5, 12, 65, 23, 31]
lista_humanos = ["Yamsha", "Goku", "Jesus", "Bush"]

# Se imprime la lista "lista_humanos"
print(lista_humanos)

# Existen muchas funciones para trabajar con listas en python
# Una de ellas es .pop() que se usa para aventar o expulsar el ultimo elemento de la lista
lista_humanos.pop()

# Se vuelve a imprimir la "lista_humanos" y le falta el ultimo elemento "Bush"
print(lista_humanos)  # ["Yamsha", "Goku", "Jesus"]
