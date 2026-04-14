soma=0
multiplicacao=1
numero=int(input("Digite um número: "))
for i in range(2, numero+1, 2):
    multiplicacao=multiplicacao*(i-1)
    soma=soma+i
print(f"A soma dos números pares de 1 a {numero} é {soma}\nA multiplicação dos números ímpares de 1 a {numero} é {multiplicacao}")