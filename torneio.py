import random

participantes = []

# cadastro de jogadores
for c in range(1,9):
    nome = input(f'Digite o nome do jogador {c}: ').upper()
    time = input(f'Digite o time escolhido por {nome}: ').upper()

    participantes.append({
        "jogador": nome,
        "time": time,
        "pontos": 0,
        "gols": 0
    })

# embaralhar jogadores
random.shuffle(participantes)

# criar grupos
grupoA = participantes[:4]
grupoB = participantes[4:]

print("\n⚽ GRUPO A")
for p in grupoA:
    print(p["jogador"], "-", p["time"])

print("\n⚽ GRUPO B")
for p in grupoB:
    print(p["jogador"], "-", p["time"])


# função de partida
def jogar_partida(j1, j2):

    gols1 = random.randint(0,5)
    gols2 = random.randint(0,5)

    print(f'{j1["jogador"]} {gols1} x {gols2} {j2["jogador"]}')

    j1["gols"] += gols1
    j2["gols"] += gols2

    if gols1 > gols2:
        j1["pontos"] += 3
    elif gols2 > gols1:
        j2["pontos"] += 3
    else:
        j1["pontos"] += 1
        j2["pontos"] += 1


# fase de grupos
print("\n🏟️ PARTIDAS GRUPO A")

for i in range(len(grupoA)):
    for j in range(i+1, len(grupoA)):
        jogar_partida(grupoA[i], grupoA[j])

print("\n🏟️ PARTIDAS GRUPO B")

for i in range(len(grupoB)):
    for j in range(i+1, len(grupoB)):
        jogar_partida(grupoB[i], grupoB[j])


# classificação
grupoA.sort(key=lambda x: x["pontos"], reverse=True)
grupoB.sort(key=lambda x: x["pontos"], reverse=True)

print("\n📊 CLASSIFICAÇÃO GRUPO A")
for p in grupoA:
    print(p["jogador"], "-", p["pontos"], "pontos")

print("\n📊 CLASSIFICAÇÃO GRUPO B")
for p in grupoB:
    print(p["jogador"], "-", p["pontos"], "pontos")


# semifinal
print("\n🔥 SEMIFINAL")

semi1_a = grupoA[0]
semi1_b = grupoB[1]

semi2_a = grupoB[0]
semi2_b = grupoA[1]


def jogar_mata_mata(j1, j2):

    while True:
        gols1 = random.randint(0,5)
        gols2 = random.randint(0,5)

        print(f'{j1["jogador"]} {gols1} x {gols2} {j2["jogador"]}')

        if gols1 > gols2:
            return j1
        elif gols2 > gols1:
            return j2
        else:
            print("Empate! Novo jogo...")


print("\nSEMIFINAL 1")
finalista1 = jogar_mata_mata(semi1_a, semi1_b)

print("\nSEMIFINAL 2")
finalista2 = jogar_mata_mata(semi2_a, semi2_b)


# final
print("\n🏆 FINAL")

campeao = jogar_mata_mata(finalista1, finalista2)

print("\n👑 CAMPEÃO DO TORNEIO")
print(campeao["jogador"], "com o time", campeao["time"])