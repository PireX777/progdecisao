'''
Crie um programa que pergunte a idade do usuário e em seguida informe se
este usuário é menor de idade ou maior de idade.
'''

idade = int(input("Informe a sua idade:"))

#lógica do op ternário1: var = (se for falso, se for verdadeiro)[teste condicional]

resposta = ("menor de idade", "maior de idade")[idade >= 18]

print("Você é ", resposta)