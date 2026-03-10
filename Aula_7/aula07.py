#Dicionarios em python 
aluno = {
    #"chaves": valor
    "nome":"Ana",
    "idade":14,
    "nota":8.5,
    "curso": "Tecnico em informatica para internet",
    #array
    "array":[30, True, "texto"],
    #adicionarip dentro de outro dicionario
    "endereço":{
        "cidade":"SP",
        "estado": "SP",
        "numero":"263"
    }
}

 #acessando valores
 #retorna nome aluno
print(aluno["nome"])
#retorna nome aluno
#acessando um campo especifico dentro de um array
print(aluno["array"])
print(aluno["array"][1])
#retorna endereço do aluno
#acessar apenas um unico campo do dicionario (endereço)
print(aluno["endereço"])
print(aluno["endereço"]["estado"])
#retorna idade do aluno
print(aluno["idade"])
#retorna nota do aluno
print(aluno["nota"])
#retorna curso do aluno
print(aluno["curso"])

#Alterar dadis do dicionario
aluno["idade"] = 20

print(aluno["idade"])
print(aluno["idade"])

#alterar dados dentro de um array que esta dentro do dicionario 
aluno["array"][2] = 9
print(aluno["array"][2])

#Alterar dados do docionario endereço que esta dentro  do dicionario aluno
aluno["endereço"]["cidade"] = "Sao Paulo"
print(aluno["endereço"])
print(aluno["endereço"]["cidade"])

#ADICIONA UM NOVO CAMPO
aluno["periodo"] = "Noturno"
print(aluno)

# Deletar uma informação 
del aluno["idade"]
print(aluno)

# Percorrer um Dicionario usando laco de repetição para  retornar as chaves
for chave in aluno:
    print(chave)
    
# Percorrer um dicionario usando laco de repetição para retornar valores 
for valor in aluno.values():
    print(valor)    

# Pecorrer um dicionario e retonar chave e valor 
for chave, valor in aluno.items():
    print(chave, ":", valor)
    