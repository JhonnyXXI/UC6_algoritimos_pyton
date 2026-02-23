idade = int(input("idade do cliente: "))
altura = int(input("altura do cliente (centimetros): "))


if idade >= 18: 
    if altura >= 160:
        print("cliente é maior de idade e tem a altura minima")
    else:
        print("O cliente esta abaixo da altura minima")
else:
    print("cliente é menor de idade")