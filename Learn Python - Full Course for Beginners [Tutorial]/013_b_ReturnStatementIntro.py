# 013_b_ReturnStatementIntro.py

# El Return Statement, es informacion que genera y regresa una funcion al ejecutarse.
def cube(x):
    return x*x*x
    # Ya no se puede poner código despues del return statement, porque ahí se para la función. 

# Asignamos el return value de cube(4) a una variable llamada result
result = cube(4)
# Imprimimos el valor de la nueva variable
print(result) # 64
