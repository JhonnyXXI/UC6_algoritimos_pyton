# dicionario com dados digitados 

nome = input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
cidade = input("Digite sua cidade:")

dados_usario = {
    "nome":nome,
    "idade": idade,
    "cidade":cidade
}
print("dicionario criado :")
print(dados_usario)

for chave, valor in dados_usario():
    print(chave, ":", valor)