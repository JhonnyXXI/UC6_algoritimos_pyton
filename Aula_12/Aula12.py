import pandas as pd

nome = str(input("Digite seu nome: "))
idade = str(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
# Criacao de um dicionario para receber os dados digitados pelo usuario

dados = {
    "nome": [nome],
    "idade": [idade] ,
    "altura":[altura]
}

# excel = pd.DataFrame(dados)

# to_execel() serve criar um nova planinha, pegar os dados digitados pelo usario  em formato DataFrame e gravar os dados na planilha criada 


# excel.to_excel("Aula_12/cadastro_aulo.xlsx", index = False)

leitura_excel = pd.read_excel("Aula12\cadastro_aluno.xlsx")

nova_linha = len(leitura_excel)

leitura_excel.loc[nova_linha ,'nome'] = dados ["nome"]
leitura_excel.loc[nova_linha, 'idade'] = dados["idade"]
leitura_excel.loc[nova_linha, 'altura'] = dados["altura"]

leitura_excel.to_excel("Aula12\cadastro_alunos.xlsx", index = False)