import pandas as pd

# Ler o Excel
try:
    leitura_excel = pd.read_excel("banco_tabajara.xlsx", dtype={"cpf": str})
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

# =========================
# CRIAR CONTA
# =========================
if opcao == "1":

    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF: ")
    tipo_conta = input("Digite o tipo de conta (Corrente, Poupança, Salario): ")

    cpf = cpf.replace(".", "").replace("-", "")

    if len(leitura_excel) == 0:
        numero_conta = 0
        agencia = 400
    else:
        numero_conta = int(leitura_excel["numero_conta"].max()) + 1
        agencia = int(leitura_excel["agencia"].max()) + 1

    nova_linha = len(leitura_excel)

    leitura_excel.loc[nova_linha, "nome_cliente"] = nome
    leitura_excel.loc[nova_linha, "tipo_conta"] = tipo_conta
    leitura_excel.loc[nova_linha, "numero_conta"] = numero_conta
    leitura_excel.loc[nova_linha, "cpf"] = cpf
    leitura_excel.loc[nova_linha, "agencia"] = agencia
    leitura_excel.loc[nova_linha, "extrato_bancario"] = 0.0
    leitura_excel.loc[nova_linha, "deposito"] = 0.0
    leitura_excel.loc[nova_linha, "saque"] = 0.0

    leitura_excel.to_excel("banco_tabajara.xlsx", index=False)

    print("\nConta criada com sucesso!")
    print("Nome:", nome)
    print("CPF:", cpf)
    print("Tipo da conta:", tipo_conta)
    print("Número da conta:", numero_conta)
    print("Agência:", agencia)
    print(f"Saldo: R$ {leitura_excel.loc[nova_linha, 'extrato_bancario']:.2f}")

# =========================
# ACESSAR CONTA
# =========================
elif opcao == "2":

    cpf = input("Digite o CPF: ")
    numero_conta = input("Digite o número da conta: ")

    cpf = cpf.replace(".", "").replace("-", "")

    cliente = leitura_excel[
        (leitura_excel["cpf"].astype(str) == cpf) &
        (leitura_excel["numero_conta"].astype(str) == numero_conta)
    ]

    if not cliente.empty:
        indice = cliente.index[0]
        nome_cliente = cliente.iloc[0]["nome_cliente"]

        print(f"\nBem-vindo {nome_cliente} ao Banco Tabajara")

        print("\n1 - Ver extrato bancário")
        print("2 - Depositar")
        print("3 - Sacar")

        opcao_conta = input("Escolha uma opção: ")

        # =========================
        # VER EXTRATO
        # =========================
        if opcao_conta == "1":
            print("\n=== EXTRATO BANCÁRIO ===")
            print("Nome:", leitura_excel.loc[indice, "nome_cliente"])
            print("Tipo da conta:", leitura_excel.loc[indice, "tipo_conta"])
            print("Número da conta:", leitura_excel.loc[indice, "numero_conta"])
            print("CPF:", leitura_excel.loc[indice, "cpf"])
            print("Agência:", leitura_excel.loc[indice, "agencia"])
            print(f"Saldo atual: R$ {float(leitura_excel.loc[indice, 'extrato_bancario']):.2f}")
            print(f"Último depósito: R$ {float(leitura_excel.loc[indice, 'deposito']):.2f}")
            print(f"Último saque: R$ {float(leitura_excel.loc[indice, 'saque']):.2f}")

        # =========================
        # DEPÓSITO
        # =========================
        elif opcao_conta == "2":
            valor = float(input("Digite o valor do depósito: "))

            leitura_excel.loc[indice, "extrato_bancario"] += valor
            leitura_excel.loc[indice, "extrato_bancario"] = round(leitura_excel.loc[indice, "extrato_bancario"], 2)
            leitura_excel.loc[indice, "deposito"] = round(valor, 2)

            leitura_excel.to_excel("banco_tabajara.xlsx", index=False)

            print("\nDepósito realizado com sucesso!")
            print(f"Valor depositado: R$ {valor:.2f}")
            print(f"Novo saldo: R$ {float(leitura_excel.loc[indice, 'extrato_bancario']):.2f}")

        # =========================
        # SAQUE
        # =========================
        elif opcao_conta == "3":
            valor = float(input("Digite o valor do saque: "))
            tipo = leitura_excel.loc[indice, "tipo_conta"]

            if tipo == "Corrente":
                taxa = valor * 0.05
            elif tipo == "Poupança":
                taxa = 0.0
            elif tipo == "Salario":
                taxa = valor * 0.02
            else:
                taxa = 0.0

            total_saque = valor + taxa
            saldo = float(leitura_excel.loc[indice, "extrato_bancario"])

            if total_saque <= saldo:
                leitura_excel.loc[indice, "extrato_bancario"] -= total_saque
                leitura_excel.loc[indice, "extrato_bancario"] = round(leitura_excel.loc[indice, "extrato_bancario"], 2)
                leitura_excel.loc[indice, "saque"] = round(valor, 2)

                leitura_excel.to_excel("banco_tabajara.xlsx", index=False)

                print("\nSaque realizado com sucesso!")
                print(f"Valor do saque: R$ {valor:.2f}")
                print(f"Taxa cobrada: R$ {taxa:.2f}")
                print(f"Total retirado da conta: R$ {total_saque:.2f}")
                print(f"Novo saldo: R$ {float(leitura_excel.loc[indice, 'extrato_bancario']):.2f}")
            else:
                print("\nSaldo insuficiente")

        else:
            print("Opção inválida")

    else:
        print("Usuário não encontrado, tentar novamente ou realizar o cadastro")

else:
    print("Opção inválida")