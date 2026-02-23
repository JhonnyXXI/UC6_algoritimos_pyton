# if, 2 elif, else para o menu
# par e impar copiar e colar
# tabuaad copia cola
# sair = break

print("digite 1 para tabuada")
print("digite 2 para par ou impar")
print("digite 3 para sair")



opcao = int(input())


if opcao == 1:
    print("tabuada")
    
    # tabuada

    while True:
        num1 = input("digite um numero: ")

        if num1.isdigit():

            num1 = int(num1)
            multiplo = 1
        
            while multiplo <= 10:

                resultado = num1 * multiplo
                print(num1, "x", multiplo, "=", resultado)
                multiplo += 1
            break
        else:
            print("numero invalido, digite novamente")


if opcao == 2:
    print("par impar")

    #par ou impar

    num2 = int(input("digite um numero"))

    for num2 in range(0, num2+1, 1):
        if num2 % 2 == 0:
                    print(num2, "par")
        else:
                    print(num2, "impar")



if opcao == 3:
    print("blablabla")
