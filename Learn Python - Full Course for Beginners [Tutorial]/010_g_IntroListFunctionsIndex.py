# 010_g_IntroListFunctionsIndex.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
lista_numeros = [1, 2, 5, 12, 65, 23, 31]
lista_humanos = ["Yamsha", "Goku", "Jesus", "Bush"]

# Se imprime la lista "lista_humanos"
print(lista_humanos)

# Existen muchas funciones para trabajar con listas en python
# Una de ellas es .index() que se usa para que nos indique el index number de un elemento especifico
# Si el elemento no existe ocurrira un error.
print(lista_humanos.index("Goku"))  # 1
print(lista_humanos.index("Jesus"))  # 2
print(lista_humanos.index("Yamsha"))  # 0

# Esto tambien lo podemos utiliar para detectar si algo existe dentro de la lista,
# si no regresa un index number es porque no existe y saldra un error.
print(lista_humanos.index("Cucuy"))  # ValueError: 'Cucuy' is not in list
