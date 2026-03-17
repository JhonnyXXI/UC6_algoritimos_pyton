import pandas as pd


print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > Adicionar")
print("         2 > Alterar")
print("         3 > Apagar")
opcao = int(input("R: "))


if opcao == 1:
    print("Opeção 1 selecionada")
    nome = str(input("Digite o seu nome: "))
    idade = int(input("Digite sua idade: "))
    altura = float(input("Digite sua altura: "))

    dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}

excel = pd.DataFrame(dados)

excel.to_excel("Aula_12/alunos.xlsx", index=False)