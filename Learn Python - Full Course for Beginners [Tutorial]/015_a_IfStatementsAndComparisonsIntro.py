# 015_a_IfStatementsAndComparisonsIntro.py

# Declaramos una funcion que recibira 3 numeros como parametros
def max_num(n1, n2, n3):
    # Luego comparara los numeros
    if n1 >= n2 and n1 >= n3:
        # regresara el valor mas grande
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

# Mandamos llamar a la función enviando 3 parametros, debe regresar el numero mas grande
print(max_num(1, 10, 4))
