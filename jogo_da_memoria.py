from random import randint
import os
os.system("cls")
from time import sleep

palavras=["dia", "bola", "casa", "flor", "noite"]
sorteio=["", "", "", "", ""]
n=0
digitadas=["", "", "", "", ""]
acertos=0

for i in range(5):
    n=randint(0, 4)
    print(palavras[n])
    sorteio[i]=palavras[n]
    sleep(1)

os.system("cls")

for i in range(5):
    digitadas[i]=input(f"Digite a {i+1} palavra: ")
    if digitadas[i]==sorteio[i]:
        acertos=acertos+1

print(f"Voce acertou {acertos} palavras")


