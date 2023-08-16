'''6) Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.'''


num1 = int(input("Me informe um número: " ))
num2 = int(input("Me informe um número: " ))

if num1 > num2:
    print("A diferença entre o maior valor e o menor valor é", (num1 - num2))
else:
    print("A diferença entre o maior valor e o menor valor é", (num2 - num1))