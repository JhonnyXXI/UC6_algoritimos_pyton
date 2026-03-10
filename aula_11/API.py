import requests
# API
url = "https://rickandmortyapi.com/api/character"


respota = requests.get(url) # retorno status 200

json = respota.json() # retonar o JSON 

print(json)

personagem = json["results"]

print(personagem)

#laço de repetição para colsutar apenas os nomes do personagens 
for nome_personagem in personagem:
    print(nome_personagem["name"])

# retorbar mais informações alem do nome 
for mais_info in personagem:
    print("nome: ", mais_info["name"])
    print("status: ",mais_info['status'])
    print("Especid: ",mais_info['species'])
    print("---------------------------------")

# pedir ao usuario para digitar um ID e retornar da API o personagem referente a esse ID 

id = int (input(" digite  um numero inteiro: "))

link_API = f"https://rickandmortyapi.com/api/character/{id}"

respota = requests.get(link_API)

novo_json= respota.json()

print("nome: ", mais_info["name"])
print("status: ",mais_info['status'])
print("Especid: ",mais_info['species'])
print("---------------------------------")