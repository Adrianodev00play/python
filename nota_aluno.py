import os
os.system("cls")
nome=str(input("Digite seu nome: "))
disciplina=str(input("Digite sua disciplina: "))
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
situacao=""
if (nota1+nota2)/2<7:
    situacao="reprovado"
else:
    situacao="reprovado"
print(f"Seu nome é: {nome}\nSua disciplina é: {disciplina}\nSua Média é {(nota1+nota2)/2} Sua situação é {situacao}")