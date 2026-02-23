while True:
    numero = input("digite um numero: ")

    if numero.isdigit():

        numero = int(numero)
        multiplo = 1
    
        while multiplo <= 2000:

            resultado = numero * multiplo
            print(numero, "x", multiplo, "=", resultado)
            multiplo += 1
        break
    else:
        print("numero invalido, digite novamente")