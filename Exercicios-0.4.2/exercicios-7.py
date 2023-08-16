'''7. Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais.'''


n1 = int(input("Informe um número: "))
n2 = int(input("Informe um número: "))

maior = n1

if maior < n2:
    maior = n2

    menor = n1

    if menor > n2:
        menor = n2

    print(f"O maior valor inserido foi {maior}")
    print(f"O menor valor inserido foi {menor}")

menor = n1

if menor > n2:
    menor = n2

    maior = n1

    if maior < n2:
        maior = n2

    print(f"O maior valor inserido foi {maior}")
    print(f"O menor valor inserido foi {menor}")

if n1 == n2:
    print("Ambos números são iguais")