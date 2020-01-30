# 010_d_IntroListFunctionsRemove.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
lista_numeros = [1, 2, 5, 12, 65, 23, 31]
lista_humanos = ["Yamsha", "Goku", "Jesus", "Bush"]

# Se imprime la lista "lista_humanos"
print(lista_humanos)

# Existen muchas funciones para trabajar con listas en python
# Una de ellas es .remove() que se usa para remover un elemento especifico
lista_humanos.remove("Goku")  # Va a remover a Goku

# Se vuelve a imprimir la "lista_humanos" pero sin el elemento "Goku"
print(lista_humanos) # ["Yamsha", "Jesus", "Bush"]
