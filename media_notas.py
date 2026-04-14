import os
os.system("cls")
n1=float(input("Digite a 1 nota: "))
n2=float(input("Digite a 2 nota: "))
n3=float(input("Digite a 3 nota: "))
n4=float(input("Digite a 4 nota: "))
n5=float(input("Digite a 5 nota: "))
media=(n1+n2+n3+n4+n5)/5
maior=max(n1, n2, n3, n4, n5)
menor=min(n1, n2, n3, n4, n5)
print(f"A média das notas é: {media}\nA maior nota é: {maior}\nA menor nota é: {menor}")