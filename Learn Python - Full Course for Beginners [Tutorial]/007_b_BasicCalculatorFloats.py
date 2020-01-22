# 007_b_BasicCalculatorFloats.py
# Ask for 2 numbers and diplay the result on the console

# Input 2 numeros y se guardan en variables num1 y num2
# input siempre convierte en string lo que recibe
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

# Tengo que convertir los numeros en float con float() para sumarlos
# Ahora se puede mandar cualquier numero porque se convertiran a floats
result = float(num1) + float(num2)
print(result)
