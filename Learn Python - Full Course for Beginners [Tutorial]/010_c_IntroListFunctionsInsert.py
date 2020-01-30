# 010_c_IntroListFunctionsInsert.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
lista_numeros = [1, 2, 5, 12, 65, 23, 31]
lista_humanos = ["Yamsha", "Goku", "Jesus", "Bush"]

# Se imprime la lista "lista_humanos"
print(lista_humanos)

# Existen muchas funciones para trabajar con listas en python
# Una de ellas es .insert() que se usa para insertar un nuevo elemento en un index number determinado
lista_humanos.insert(1,"Roshi") # Primer parametro es el index y el segundo el elemento a insertar

# Se vuelve a imprimir la "lista_humanos" pero con el nuevo elemento agregado en el index 1
# Y todos los demas elementos despues del index 1 se mueven +1
print(lista_humanos) # ["Yamsha", "Roshi", "Goku", "Jesus", "Bush"]
