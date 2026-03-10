#  dados do aluno
nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite la nota 2: "))
nota3 = float(input("Digite la nota 3: "))
nota4 = float(input("Digite la nota 4: "))
nota5 = float(input("Digite la nota 5: "))

# Criando o dicionário
aluno = {
    "nome": nome,
    "nota1": nota1,
    "nota2": nota2,
    "nota3": nota3,
    "nota4": nota4,
    "nota5": nota5
}


media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5


print("Dados do aluno:")
print(aluno)

print(f"Média do aluno: {media:.2f}")

