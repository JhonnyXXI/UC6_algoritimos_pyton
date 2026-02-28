
nomes = []


for i in range(4):
    nome = input("Digite um nome: ")
    nomes.append(nome)

remover = input("Digite um nome para remover: ")


if remover in nomes:
    nomes.remove(remover)
    print("Nome removido com sucesso!")
else:
    print("Nome não encontrado")

print("Lista final:", nomes)