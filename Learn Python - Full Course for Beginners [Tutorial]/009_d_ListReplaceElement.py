# 009_d_ListReplaceElement.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
listOfRandom = ["Larry", 500, 0.25, 0.00005, True, "Leon", False]

# Se imprime el primer elemento con index 0 = Larry
print(listOfRandom[0])

# Se puede reemplazar un elemento de la lista como si fuera una variable
# Primero se selecciona el elemento usando su index number [#]
# Y luego se le asigna otro valor listName[#] = value
listOfRandom[0] = "Jerry"

# Se imprime el primer elemento con index 0, que ahora es "Jerry"
print(listOfRandom[0])
