import os
os.system("cls")
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2

if media<7:
    print("Sua media foi: ",media," \nReprovado")

else:
    print("Sua média é: ",media," \nAprovado")