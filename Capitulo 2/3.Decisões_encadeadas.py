nome= input("Digite um nome: ")
idade= int(input("Digite sua idade: "))
doença_grave=input("Suspeita de doença? ")

if idade>=65:
    print("O paciente" , nome , "DEVE IR NA FRENTE")
     
elif doença_grave=="SIM":
    print("O paciente" , nome , "deve-ser levado a sala  de espera")

else:
    print("O paciente" , nome , "não tem preferência")
