# 010_j_IntroListFunctionsCopy.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
lista_numeros = [1, 2, 5, 12, 65, 23, 31]
lista_humanos = ["Yamsha", "Goku", "Goku", "Goku", "Jesus", "Bush"]

# Existen muchas funciones para trabajar con listas en python
# Una de ellas es .copy() que se usa para copiar una lista
# Primero se crea una nueva variable que copiara el contenido de otra lista. 
lista_numeros2 = lista_numeros.copy()

# Luego las mandamos imprimir. lista_numeros2 copio el contenido de lista_numeros
print(lista_numeros)  # [1, 2, 5, 12, 65, 23, 31]
print(lista_numeros2)  # [1, 2, 5, 12, 65, 23, 31]
