import random

nomes = []
times = []

for c in range(1,5):
    nome = input(f'Digite o nome do jogador {c}: ').upper()
    time = input(f'Digite o time que {nome} escolheu: ').upper()

    nomes.append(nome)
    times.append(time)

times_sorteados = times.copy()

while True:
    random.shuffle(times_sorteados)

    erro = False

    for i in range(len(nomes)):
        if times_sorteados[i] == times[i]:
            erro = True
            break

    if not erro:
        break

print('\nSORTEIO FINAL\n')

for i in range(len(nomes)):
    print(f'{nomes[i]} ficou com o time {times_sorteados[i]}')