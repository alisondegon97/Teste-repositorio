import random

cont = 0
nomes = []
times = []

for c in range(1, 5):
    nome = str(input('Digite o nome de pessoa {}: \n'.format(c))).upper()
    time = str(input('Digite o nome do time que {} escolheu: \n'.format(nome))).upper()
    cont += 1 
    nomes.append(nome)
    times.append(time)

for c in range (1, 5):
    computadortime = random.choice(times)
    computadornome = random.choice(nomes)
    print('Computador escolheu o jogador {} joga com o time {}: '.format(computadornome, computadortime))
    times.remove(computadortime)
    nomes.remove(computadornome)

