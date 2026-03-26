import pandas as pd

try:
    leitura_excel = pd.read_excel("banco_tabajara.xlsx")
except:
    leitura_excel = pd.DataFrame(columns=[
        "nome_cliente",
        "tipo_conta",
        "numero_conta",
        "cpf",
        "agencia",
        "extrato_bancario",
        "deposito",
        "saque"
    ])

print("\n=== BANCO TABAJARA ===")
print("1 - Criar conta")
print("2 - Acessar conta")

opcao = input("Escolha uma opção: ")

# CRIAR CONTA

if opcao == "1":

    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF: ")
    tipo_conta = input("Digite o tipo de conta (Corrente, Poupança, Salario): ")

    cpf = cpf.replace(".", "").replace("-", "")

    if len(leitura_excel) == 0:
        numero_conta = 0
        agencia = 400
    else:
        numero_conta = leitura_excel["numero_conta"].max() + 1
        agencia = leitura_excel["agencia"].max() + 1

    nova_linha = len(leitura_excel)

    leitura_excel.loc[nova_linha, "nome_cliente"] = nome
    leitura_excel.loc[nova_linha, "tipo_conta"] = tipo_conta
    leitura_excel.loc[nova_linha, "numero_conta"] = numero_conta
    leitura_excel.loc[nova_linha, "cpf"] = cpf
    leitura_excel.loc[nova_linha, "agencia"] = agencia
    leitura_excel.loc[nova_linha, "extrato_bancario"] = 0
    leitura_excel.loc[nova_linha, "deposito"] = 0
    leitura_excel.loc[nova_linha, "saque"] = 0

    leitura_excel.to_excel("banco_tabajara.xlsx", index=False)

    print("\nConta criada com sucesso!")
    print("Nome:", nome)
    print("Conta:", numero_conta)

# ACESSAR CONTA

elif opcao == "2":

    cpf = input("Digite o CPF: ")
    numero_conta = input("Digite o número da conta: ")

    cpf = cpf.replace(".", "").replace("-", "")

    cliente = leitura_excel[
        (leitura_excel["cpf"].astype(str) == cpf) &
        (leitura_excel["numero_conta"].astype(str) == numero_conta)
    ]

    if not cliente.empty:
        nome_cliente = cliente.iloc[0]["nome_cliente"]
        print(f"Bem-vindo {nome_cliente} ao Banco Tabajara")
    else:
        print("Usuário não encontrado")

else:
    print("Opção inválida")