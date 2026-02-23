'''
nome = input("qual é o seu nome? ")

print ("seu nome é: ", nome)
'''


# int=inteiro
# float=decimal

'''
nota1 = int(input("nota 1: "))
nota2 = int(input("nota 2: "))
nota3 = int(input("nota 3: "))

media = (nota1 + nota2 + nota3) / 3

print("a media é: ", media)
'''

preco = float(input("preço do produto: "))
desconto = int(input("desconto"))

preco_final = preco - preco * (desconto / 100)

print(preco_final)