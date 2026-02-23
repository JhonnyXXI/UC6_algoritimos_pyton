nota1 = int(input("nota 1: "))
nota2 = int(input("nota 2: "))
nota3 = int(input("nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print("Sua media é: ", media)

if media >= 6:
    print("APROVADO!!!")

else:
    print("REPROVADO!!!")