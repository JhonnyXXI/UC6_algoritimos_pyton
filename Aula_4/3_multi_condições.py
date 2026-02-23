nome = input ("nome do aluno: ")

nota1 = int(input("nota 1: "))
nota2 = int(input("nota 2: "))
nota3 = int(input("nota 3: "))

media = int((nota1 + nota2 + nota3) / 3)

if media >= 9: 
    print ("o aluno", nome, "tirou", media, "e foi aprovado com exelencia")

elif media >= 7:
    print ("o aluno", nome, "tirou", media, "e foi aprovado")

elif media >= 5:
    print ("o aluno", nome, "tirou", media, "e foi aprovado com exito")

else :
    print ("o aluno", nome, "tirou", media, "e foi reprovado")