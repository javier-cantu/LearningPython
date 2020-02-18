# 015_b_IfStatementsAndComparisonsIntro.py

# Una forma menos eficiente pero que se entiende mejor uso solo if 
# Declaramos una funcion que recibira 3 numeros como parametros
def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    if n2 >= n1 and n2 >= n3:
        return n2
    if n3 >= n1 and n3 >= n2:
        return n3

# Mandamos llamar a la función enviando 3 parametros, debe regresar el numero mas grande
print(max_num(1, 10, 44))
