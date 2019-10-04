import random, csv

lista1 = ['b', 'c', 'd', 'f', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z']
lista2 = ['e', 'u', 'i', 'a', 'o']

with open("arquivos/saida.csv", 'w', newline='') as saida:
    escrever = csv.writer(saida)
    for i in range(1000):

        inicio = 'sudo'
        letra1 = random.choice(lista1)
        letra2 = random.choice(lista2)
        letra3 = random.choice(lista1)
        letra4 = random.choice(lista2)
        fim = 'api'
        nome = inicio + letra1 + letra2 + letra3 + letra4 + fim
        escrever.writerow([nome])
        i =+ 1


