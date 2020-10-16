print("********")
print("Bem vindo ao Bacará!")
print("********")

fichas = 100

print(f'Você começará o jogo com {fichas} fichas. Boa sorte')

quantos_baralhos = int(input("Você quer jogar com quantos baralhos? (1/6/8)"))

quantos_jogadores = int(input("Quantos jogadores vão participar? "))

game_on = True

while game_on:
    quem_aposta = input('Em quem você deseja apostar? (jogador/banco/empate)')
    fichas_apostadas = int(input("Quantas fichas você deseja apostar? "))


    carta1_jogador, valor1_jogador = sorteia_carta(quantos_baralhos, baralho)
    carta2_jogador, valor2_jogador = sorteia_carta(quantos_baralhos, baralho)
    carta1_banco, valor1_banco = sorteia_carta(quantos_baralhos, baralho)
    carta2_banco, valor2_banco = sorteia_carta(quantos_baralhos, baralho)
