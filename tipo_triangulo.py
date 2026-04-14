A=float(input("Digite um número: "))
B=float(input("Digite um número "))
C=float(input("Digite um número: "))
if A==B and A==C:
    print("Triângulo equilátero")
elif A!=B and A!=C and B!=A and B!=C and C!=A and C!=B:
    print("Triângulo escaleno")
elif A==B and A!=C or A==C and A!=B or B==A and B!=C or B==C and B!=A or C==A and C!=B or C==B and C!=A:
    print("Triângulo isóscele")