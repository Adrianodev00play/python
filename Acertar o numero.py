import os
os.system("cls")
from random import randint
numero=0
sorteado = randint(1, 10)

while numero != sorteado:
    numero = int(input("Digite um número: "))

    if numero > sorteado:
        print("O número sorteado é menor que esse número")
    else:
        if numero< sorteado:
            print("O número sorteado é maior que esse número")

print("Voce acertou o número!")