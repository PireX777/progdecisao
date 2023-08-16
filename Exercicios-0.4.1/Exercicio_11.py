'''11) Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.'''

num = int(input("Informe um número de três algarismos: "))

if ( num >=100 and num <=999 ):

    cent = num // 100
    print(f"O algarismo das centenas de {num} é {cent}")

else:
        print(f"O valor informado não possui 3 algarismos!")
