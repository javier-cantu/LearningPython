# 012_c_Functions2Parameters.py

# A una funcion se le puede dar información que se llama "parameters"
# Se pueden mandar mas de un parameter

# El parametro se nombra dentro del parentesis al definir la funcion
# El parametro es como una variable que se usa dentro de la funcion
def print_name_age(name, age):
    print("Hello " + name + " you are " + str(age) + " years old")

# Asi se llama la funcion enviando un parametro
print_name_age("Brian", "22") # Hello Brian you are 22 years old
print_name_age("Arnold", "76") # Hello Arnold you are 76 years old
