import random, time, os


def dice(side):
    roll = random.randint(1, side)
    return roll


def name(contador):
    os.system("clear")
    contador += 1
    name = input(f"Qual será o nome do {contador}º personagem?\nNOME > ")
    print(f"Nós saudamos ó grande guerreiro(a) {name}!")
    time.sleep(1)
    return name


def classes(tipo):
    global escolha
    if tipo == 1:
        escolha = 'Humano'
        tipo = print(f"Você selecionou {escolha}!")
    elif tipo == 2:
        escolha = 'Anão'
        tipo = print(f"Você selecionou {escolha}!")
    elif tipo == 3:
        escolha = 'Mago'
        tipo = print(f"Você selecionou {escolha}!")
    elif tipo == 4:
        escolha = 'Elfo'
        tipo = print(f"Você selecionou {escolha}!")
    elif tipo == 5:
        escolha = 'Troll'
        tipo = print(f"Você selecionou {escolha}!")
    return escolha


def personagem():
    escolha = input(
        "Qual será o tipo do seu personagem?\nDigite 1 para Aleatório ou 2 para escolher através de uma lista.\nESCOLHA > ")
    if escolha == '1':
        print()
        tipo = random.randint(1, 5)
        escolha = classes(tipo)
        return escolha
    elif escolha == '2':
        while True:
            print()
            tipo = input("1 - Humano\n2 - Anão\n3 - Mago\n4 - Elfo\n5 - Troll\n> ")
            tipo = int(tipo)
            os.system("clear")
            if 1 <= tipo <= 5:
                classes(tipo)
                break
            else:
                print("Digite apenas números entre 1 ou 5.")
                continue


def vida():
    hp = ((random.randint(1, 6) * random.randint(1, 12)) / 2.0) * 100
    print(f"HP: {hp:.1f}")
    return hp


def forca():
    atq = ((random.randint(1, 6) * random.randint(1, 12)) / 2.0) + 12
    print(f"Ataque: {atq:.1f}")
    return atq


print("*** EPB - EPIC PYTHON BATTLE ***")
time.sleep(1)
print("Criação de Personagem")
time.sleep(1)

numero_personagens = int(input("Digite a quantidade de personagens que serão criados:\n> "))

nome_personagem = []
num_personagem = []
vida_personagem = []
forca_personagem = []

for i in range(0, numero_personagens):
    nome_personagem.append(name(contador=i))
    num_personagem.append(personagem())
    vida_personagem.append(vida())
    forca_personagem.append(forca())
    print("\nQue a sorte esteja a seu favor, bravo guerreiro(a)!\n")
    time.sleep(2)
    os.system("clear")

while True:
    num = random.randint(0, numero_personagens - 1)
    num2 = random.randint(0, numero_personagens - 1)
    while num2 == num:
        num2 = random.randint(0, numero_personagens - 1)

    p1 = nome_personagem[num]
    p2 = nome_personagem[num2]
    hp1 = vida_personagem[num]
    hp2 = vida_personagem[num2]
    atq1 = forca_personagem[num]
    atq2 = forca_personagem[num2]

    os.system("clear")
    print(
        f"Dois dos mais bravos guerreiros criados serão selecionados a lutarem até a morte!\nSão eles os jogadores:{p1} e {p2}")
    print("\nQue comecem os jogos!\n")
    time.sleep(3)
    break

rodadas = 1
while True:
    primeiro_jogador = dice(6)
    segundo_jogador = dice(6)
    while segundo_jogador == primeiro_jogador:
        segundo_jogador = dice(6)

    if primeiro_jogador < segundo_jogador:
        print(f"{p2} ganha o {rodadas}º round!")
        rodadas += 1
        print(f"{p1} leva {atq2} de dano.\nFicando apenas com {hp1 - atq2} de HP.\n")
        hp1 -= atq2
        if hp1 <= 0:
            print(f"{p2} É O VENCEDOR!")
            exit()
    elif segundo_jogador < primeiro_jogador:
        print(f"{p1} ganha o {rodadas}º round!")
        rodadas += 1
        print(f"{p2} leva {atq1} de dano.\nFicando apenas com {hp2 - atq1} de HP.\n")
        hp2 -= atq1
        if hp2 <= 0:
            print(f"{p1} É O VENCEDOR!")
            exit()