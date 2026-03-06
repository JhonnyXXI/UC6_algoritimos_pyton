def funcao (num1, num2):
    return num1 + num2


idade = int(input("digite sua idqade"))

if idade >= 18:
    num1 = int(input("numero 1: "))
    num2 = int(input("numero 2: "))
    resultado = funcao(num1, num2)
    print("o resultado é", resultado)


else:

    print("voce é menor de idade")