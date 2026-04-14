import os
os.system("cls")
produto=1
valor=0
while produto!=0:
    produto=float(input("Digite o valor da compra: "))
    valor=valor+produto 
print(f"Sua compra deu {valor} reais\n\n--Formas de pagamento--\nDigite 1 para pagar a vista\nDigite 2 para pagar no cartão")
forma=int(input("\nDigite a forma de pagamento: "))
if forma==1:
    print(f"Valor a ser pago: {valor-(valor*0.1)} reais")
elif forma==2:
    parcelas=int(input("Digite o total de parcelas: "))
    if parcelas==1:
        print(f"Valor a ser pago: {valor}")
    elif parcelas==2:
        print(f"Valor a ser pago: {valor+(valor*0.05)} reais")
    else:
        print("Número de parcelas inválido")
else:
    print("Forma de pagamento inválida")