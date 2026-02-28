"""
dicionario {} -> Para acessar dados usamos o nome da chave 
lista [] -> Para acessar dados usamos a posicao da lista 
"""
notas = [10, 8, 5, 10, True, 7, "Andre"]
#         0  1  2   3    4   5     6 

notas.append("SENAC")
print(notas)

notas.insert(0, False)
print(notas)

#nova_lista = ["Ola mundo", 1999, 2800]
#tudo_junto = []
#todo_junto = nova_lista.extend(notas)
#nova_lista.extend(notas)

notas.remove(10)
print(notas)
notas.remove(True)
print(notas)
notas.remove("SENAC")
print(notas)
#notas.remove("andre")
# o metodo remove e case sensitive

nomes_numeros = [390, "Adenilson", 19, "Anna", 45, "Iara",390]
# POP
# nomes_numeros.pop(2)
# print(nomes_numeros)
# # CLEAR
# print(nomes_numeros.clear())
# INDEX
print(nomes_numeros.index("Adenilson"))
print(nomes_numeros)

print(nomes_numeros.count(390))

numero = [34, 45, 67, 89, 43, 44, 26, 58, 66, 33, 90]
numero.sort()
print(numero)
# Reverse
numero.reverse()
print(numero)

nome = ["Adenilson", "Anna", "Beatriz","Joao Paulo", "Joao Pedro" ,"Aline"]
nome.sort()
print(nome)