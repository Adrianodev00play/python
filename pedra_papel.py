import os
os.system("cls")
print("---PEDRA PAPEL TESOURA---")
a=str(input("Jogador A: "))
b=str(input("Jogador B: "))
if a=="pedra" and b=="tesoura" or a=="papel" and b=="pedra" or a=="tesoura" and b=="papel":
    print("O jogador A venceu")
elif a=="tesoura" and b=="pedra" or a=="pedra" and b=="papel" or a=="papel" and b=="tesoura":
    print("O jogador B venceu")
elif a==b:
    print("Empate")
else:
    print("Caracteres inválidos")