# 010_h_IntroListFunctionsSort.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
lista_numeros = [1, 2, 5, 12, 65, 23, 31]
lista_humanos = ["Yamsha", "Goku", "Goku", "Goku", "Jesus", "Bush"]

# Se imprimen las listas en el orden original
print(lista_humanos)
print(lista_numeros)

# Existen muchas funciones para trabajar con listas en python
# Una de ellas es .sort() que se usa para ordenar la lista en forma ascendente
# Orden alfabetico, o numerico
# Primero se ordenan con sort()
lista_humanos.sort()
lista_numeros.sort()

# Luego las mandamos imprimir ordenadas. Si ponemos print(lista_humanos.sort()) sale None
print(lista_humanos)
print(lista_numeros)
