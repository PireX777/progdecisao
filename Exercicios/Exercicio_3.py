'''3) Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar.'''

num = int(input("Escolha um número: "))

num1 = num%2

if (num1 == 1):
    print("é impar")

else:
    print("é par")