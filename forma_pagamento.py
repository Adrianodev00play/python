import os
os.system("cls")
valor = float(input("Digite o valor: "))

print("\n----FORMA DE PAGAMENTO----\nDigite 1: a vista\nDigite 2: cartão")

forma=int(input("\nDigite a forma de pagamento: "))
if forma==1:
    print(f"Valor a ser pago {valor-(valor*0.05)}")
else:
    if forma==2:
        print("\n----PARCELAMENTO----\nDigite 1: 1 parcela\nDigite 2: 2 parcelas")
parcelas=int(input("Digite a quantidade de parcelas: "))
if parcelas==1:
    print(f"\nValor a ser pago: {valor}")
else:
    if parcelas==2:
        print(f"\nValor a ser pago: {valor+(valor*0.05)}")