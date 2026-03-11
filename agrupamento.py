import random

jogadores = []
times = []

# cadastro
for c in range(1,5):
    nome = input(f'Digite o nome do jogador {c}: ').upper()
    time = input(f'Digite o time escolhido por {nome}: ').upper()

    jogadores.append(nome)
    times.append(time)

# embaralhar times
random.shuffle(times)

# criar lista jogador + time
participantes = []

for i in range(len(jogadores)):
    participantes.append({
        "jogador": jogadores[i],
        "time": times[i]
    })

# embaralhar jogadores para criar grupos
random.shuffle(participantes)

print("\nSORTEIO DOS TIMES\n")

for p in participantes:
    print(p["jogador"], "joga com", p["time"])

# criar grupos
grupoA = participantes[:2]
grupoB = participantes[2:]

print("\nGRUPO A")
for p in grupoA:
    print(p["jogador"], "-", p["time"])

print("\nGRUPO B")
for p in grupoB:
    print(p["jogador"], "-", p["time"])

# confrontos
print("\nCONFRONTO GRUPO A")
print(grupoA[0]["jogador"], "x", grupoA[1]["jogador"])

print("\nCONFRONTO GRUPO B")
print(grupoB[0]["jogador"], "x", grupoB[1]["jogador"])