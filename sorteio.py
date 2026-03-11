nomes = []
times = []

for c in range(1,5):
    n = input('Digite o nome da pessoa {}: \n'.format(c)).upper()
    t = input('Digite o nome do time que {} escolheu: \n'.format(n)).upper()

    nomes.append(n)
    times.append(t)

for c in range(4):
    print(nomes[c], '-', times[c])