numero = int(input("digite um numero"))

for numero in range(0, numero+1, 1):
    if numero % 2 == 0:
        print(numero, "par")
    else:
        print(numero, "impar")