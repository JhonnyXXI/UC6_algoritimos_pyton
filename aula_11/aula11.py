import random
import math 
import datetime
numero_aleatorio = random.randint(1000, 2000)

print(numero_aleatorio)

# sorteio de aluno
alunos  = ["Israel", "Adenilson","Anna","wellington","Jonathan", "Isabelly","João Paulo","João Pedro", "Luis Felipe", "Iara", " Vanessa", "Daniel", "Lucas", "Bernado", "Camila", " Stefany", "Guilherme", "Micael", "kauan"]
sorteado = random.choice(alunos)
sorteado2 = random.choice(alunos)

print("Dupla Dinamica", sorteado, " - " , sorteado2)


numero = 16 
raiz = math.sqrt(numero)
print(raiz)

# Elevar um numero 
print(math.pow(2, 2))

# trabalhando com datas 
agora = datetime.datetime.now()
print(agora)

# Exercicio
# Solicitar ao usuario um numero de 1 até 5
# Gerar um numero aleatorio  a biblioteca rondom.randint
# Verificar se o usuario digitou o mesmo valor que o resultado da função rendint

numero_usuario = int(input("Digite um numero da sorte de 1 até 5 "))
numero_sorte = random.randint(1, 5)

if numero_usuario == numero_sorte:
    print("PARABENS , VOCE GANHOU ")
else:
    print("Errou, teste novamente")    