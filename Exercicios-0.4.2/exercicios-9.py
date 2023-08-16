'''9. Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos.
'''

idade = int(input("Informe sua idade: "))

resposta = ("menor de idade", "maior de 65 anos", "maior de idade" )[idade >= 18] or [idade >= 65]

print("Você é",resposta)