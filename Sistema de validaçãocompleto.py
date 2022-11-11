print("==============Bem vindo ao  Banco Juliano!!=================")
nome1 = input("Informe seu nome :")
nome2 = input("Informe  novamente seu nome:")
senha = int(input("Informe sua senha:"))
senha2 = int(input("Informe novamente sua senha"))
idade = int(input("Informe sua idade:"))
salario = float(input("Informe seu salario:"))
sexo = input("Informe seu sexo com m/f:")
email = input("Informe seu email:")
email2 = input("Informe novamente seu email:")
estado = input("Informe seu estado civil:")



while nome1  != nome2:
    print("Nome  invalido!")
    nome1 = input("Informe seu nome:")
    nome2 = input("Informe Novamente seu nome:")
print("Nome validado!\n")

while  senha != senha2 :
    print("Senha  invalida!")
    senha = int(input("Informe  sua senha:"))
    senha2 = int(input("Informe Novamente sua senha:"))
print("Senha validada!")

    
while idade >= 110 or idade < 0:   
    print("idade invalida")
    idade = int(input("Digite uma idade valida :"))
    if  idade >= 16 :
        print("Voce  é maior de idade!")
print("Idade validada com sucesso!\n")
 
while salario <= 0:
    salario = int(input("Informe seu salario novamente:"))
print("Salario valido!")
while  sexo != "m" and sexo != "f":
    print("Informe um sexo valido!!")
    sexo = input("Informe novamente  seu sexo com m/f:")
print("Sexo validado com  sucesso\n")

while email != email2:
    print("Email invalido!")
    email = input("Informe seu email:")
    email2 = input("Informe novamente seu email:")
print("Email validado com sucesso!\n")
while estado != "s" and estado != "c" and estado != "v" and estado !=  "d":
    print("valor inválido!")
    estado = input("Informe novamente seu estado civil:")

print("Todos os dados foram  validados com sucesso!\n\n\n\n")
    
