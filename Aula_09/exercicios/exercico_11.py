# funcao que receba n notas, calcule e retone a media
# funcao que recebe a media e retorna se passou ou reprovou
notas = []

num_notas = int(input("qunatas notas?: "))

def cal_media(notas):

    for i in range (num_notas):
        notas.append(int(input("digite uma nota: ")))

    return sum(notas) / len(notas)

media = cal_media(notas)
print(media)


def resultado(num_media):
    if num_media >= 6:
        print("aprovado")
    else:
        print("reprovado")


print(resultado(media))
print(notas)

# sumir com o none
# input media minima