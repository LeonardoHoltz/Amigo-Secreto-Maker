import random

entrada = open("amigos.txt", "r")
lista_amigos = []
numero_amigos = 0
for line in entrada:
    lista_amigos.append(line)
    numero_amigos += 1
entrada.close()

random.shuffle(lista_amigos)
nome_saida = "saida"

for amigo in range(numero_amigos):
    nome_saida += str(amigo)
    nome_saida += ".txt"
    saida = open(nome_saida, "w")
    saida.write(lista_amigos[0])
    lista_amigos.remove(lista_amigos[0])
    saida.close()
    nome_saida = "saida"
