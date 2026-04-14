import os
os.system("cls")
soma=0
for i in range(1001):
    if i%2==0:
        soma=soma
    else:
        soma=soma+i
print(f"A soma dos números de 1 a 100 é: {soma}")