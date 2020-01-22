# 009_c_ListSelectSomeElements.py

# Una lista es una estructura para guardar informacion
# Puede almacenar cualquier tipo de variable, int, float, string, bool
listOfRandom = ["Larry", 500, 0.25, 0.00005, True, "Leon", False]

# Para seleccionar varios elementos de una lista se usan los index numbers entre " : "
print(listOfRandom[1:4])  # Se mostraran los elementos del index 1 al 3 (no se muestra el 4) "[500, 0.25, 0.00005]"

print(listOfRandom[2:])  # Si solo se deja : despues de un index, se mostraran el resto de los elementos
