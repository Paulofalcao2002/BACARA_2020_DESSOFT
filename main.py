print("********")
print("Bem vindo ao Bacará!")
print("********")

fichas = 100

print(f'Você começará o jogo com {fichas} fichas. Boa sorte')

#variaveis que guardam o número de baralhos e jogadores na partida
quantos_baralhos = int(input("Você quer jogar com quantos baralhos? (1/6/8) "))
quantos_jogadores = int(input("Quantos jogadores vão participar? "))

#variaveis que indentificam os jogadores e quanto de fichas eles tem
numero_jogadores = []
lista_fichas_jogadores = []

for i in range(quantos_jogadores):
    numero_jogadores.append(i + 1)
    lista_fichas_jogadores.append(fichas)
    
game_on = True

while game_on:
    quem_aposta = input('Em quem você deseja apostar? (jogador/banco/empate)')
    fichas_apostadas = int(input("Quantas fichas você deseja apostar? "))


    carta1_jogador, valor1_jogador = sorteia_carta(quantos_baralhos, baralho)
    carta2_jogador, valor2_jogador = sorteia_carta(quantos_baralhos, baralho)
    carta1_banco, valor1_banco = sorteia_carta(quantos_baralhos, baralho)
    carta2_banco, valor2_banco = sorteia_carta(quantos_baralhos, baralho)
    
 texto_jogador, soma_jogador = confere_terceira_carta(valor1_jogador, valor2_jogador, carta1_jogador, carta2_jogador, 'jogador')
    texto_banco, soma_banco = confere_terceira_carta(valor1_banco, valor2_banco, carta1_banco, carta2_banco, 'banco')

    print(texto_jogador)
    print(texto_banco)

    if quem_aposta == 'jogador': fichas = aposta_jogador(soma_jogador, soma_banco, fichas, fichas_apostadas, quantos_baralhos)
    if quem_aposta == 'banco': fichas = aposta_banco(soma_jogador, soma_banco, fichas, fichas_apostadas, quantos_baralhos)
    if quem_aposta == 'empate': fichas = aposta_empate(soma_jogador, soma_banco, fichas, fichas_apostadas, quantos_baralhos)

    print(f'Seu número de fichas é {fichas}')

    if fichas_zeraram(fichas):
        print('Suas fichas acabaram!')
        break

    continua = input("Quer continuar jogando? (sim/não)")
    if continua == 'não': break
