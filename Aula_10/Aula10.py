# Abrir arquivo
# open("nota.txt", "w")

# Abrir um arquivo e Digitar informacoes
with open("Aula10/nota.txt", "w") as nota_aluno:
    nota_aluno.write("Evidentemente, o acompanhamento das preferências de consumo promove a alavancagem de alternativas às soluções ortodoxas.")

# Ler um arquivo
with open("Aula10/nota.txt", "r") as leitura_arquivo:
    recebe_texto = leitura_arquivo.read()
    print(recebe_texto)

# Adicionar um texto ao final do seu arquivo
with open("Aula10/nota.txt", "a") as adiciona_novo_texto:
    adiciona_novo_texto.write("\n Aqui tem uma nova linha de texto")