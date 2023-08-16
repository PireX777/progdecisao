'''10. Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:'''

nome = input("Informe seu Nome: ")
nota1 = float(input("Informe sua nota na prova 1: "))
nota2 = float(input("Informe sua nota na prova 2: "))

media = nota1 + nota2 / 2

if media < 3.0:
    print("Você está reprovado")
elif media > 3.0 and media < 6.9:
    print("Você está de prova final")
else:
    print("Você está aprovado")