import time
nome=input("digite seu nome: ")
idade=int(input("qual sua idade: "))
if idade>65:
    print("O mano: ", nome, "pode furar a fila.")
else:
    print("o mano", nome, "tem, q ficar quietinho")
print("===========")
time.sleep(5)
print("Obrigado pode se retirar")