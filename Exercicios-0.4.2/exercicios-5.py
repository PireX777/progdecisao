'''5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.'''

est = input("Informe a sigla de um estado brasileiro: ")


if est == 'ES' or est == 'MG' or est == 'RJ' or est == 'SP':
    print("O estado inserido está na Região Sudeste")
else:
    print("O estado inserido não está na Região Sudeste")