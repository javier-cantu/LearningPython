# 007_a_BasicCalculatorInts.py
# Ask for 2 numbers and diplay the result on the console

# Input 2 numeros y se guardan en variables num1 y num2
# input siempre convierte en string lo que recibe 
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

# Tengo que convertir los numeros en int con int() para sumarlos 
# Pero si en uno de los inputs se mando un float ocurrira un error
result = int(num1) + int(num2)
print(result)
