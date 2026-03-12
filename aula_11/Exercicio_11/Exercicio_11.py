import requests


url = "https://rickandmortyapi.com/api/character"


print("===== MENU =====")
print("1 - Consultar por ID")
print("2 - Consultar por nome")
print("3 - Lista de personagens")

opcao = input("Escolha uma opção: ")

# ---------------------------------
# OPÇÃO 1 - CONSULTAR POR ID
# ---------------------------------
if opcao == "1":

    id = int(input("Digite o ID do personagem: "))

    link_api = f"https://rickandmortyapi.com/api/character/{id}"

    resposta = requests.get(link_api)

    dados = resposta.json()

    print("\n===== PERSONAGEM =====")
    print("ID:", dados["id"])
    print("Nome:", dados["name"])
    print("Status:", dados["status"])
    print("Espécie:", dados["species"])
    print("Gênero:", dados["gender"])
    print("Origem:", dados["origin"]["name"])
    print("Localização:", dados["location"]["name"])
    print("Imagem:", dados["image"])


# ---------------------------------
# OPÇÃO 2 - CONSULTAR POR NOME
# ---------------------------------
elif opcao == "2":

    nome = input("Digite o nome do personagem: ")

    resposta = requests.get(url)

    dados = resposta.json()

    print("\n===== RESULTADO =====")

    for personagem in dados["results"]:

        if nome.lower() in personagem["name"].lower():

            print("ID:", personagem["id"])
            print("Nome:", personagem["name"])
            print("Status:", personagem["status"])
            print("Espécie:", personagem["species"])
            print("Gênero:", personagem["gender"])
            print("Origem:", personagem["origin"]["name"])
            print("Localização:", personagem["location"]["name"])
            print("Imagem:", personagem["image"])
            print("----------------------------")


# ---------------------------------
# OPÇÃO 3 - LISTAR PERSONAGENS
# ---------------------------------
elif opcao == "3":

    resposta = requests.get(url)

    dados = resposta.json()

    print("\n===== LISTA DE PERSONAGENS =====")

    for personagem in dados["results"]:

        print("ID:", personagem["id"])
        print("Nome:", personagem["name"])
        print("Status:", personagem["status"])
        print("Espécie:", personagem["species"])
        print("Gênero:", personagem["gender"])
        print("Origem:", personagem["origin"]["name"])
        print("Localização:", personagem["location"]["name"])
        print("Imagem:", personagem["image"])
        print("----------------------------")

else:
    print("Opção inválida")


print("Ola Mundo ")