import os
from baralhos import sorteia_carta, baralho
from somas import confere_terceira_carta_jogador, confere_terceira_carta_banco
from fichas import aposta_jogador, aposta_banco, aposta_empate, atualiza_fichas

print("********")
print("Bem vindo ao Bacará!")
print("********")

fichas = 100

print(f'Você começará o jogo com {fichas} fichas. Boa sorte')

#variaveis que guardam o número de baralhos e jogadores na partida
quantos_baralhos = int(input("Você quer jogar com quantos baralhos? (1/6/8) "))
quantos_jogadores = int(input("Quantos jogadores vão participar? "))

#variaveis que indentificam os jogadores e quanto de fichas eles têm
numero_jogadores = []
lista_fichas_jogadores = []

for i in range(quantos_jogadores):
    numero_jogadores.append(i + 1)
    lista_fichas_jogadores.append(fichas)
    
#laço de repetição para gerar as rodadas da partida
game_on = True
while game_on:

    #listas que guardam informacoes dos jogadores referentes a rodada
    lista_quem_aposta = []
    lista_fichas_apostadas = []
 
#Preenchendo as listas com valores
    for i in range(quantos_jogadores):
        quem_aposta = input(f'Jogador {numero_jogadores[i]}, em quem você deseja apostar? (jogador/banco/empate) ')
        lista_quem_aposta.append(quem_aposta)
        numero_valido = True
        while numero_valido:
            fichas_apostadas = int(input(f"Jogador {numero_jogadores[i]}, quantas fichas você deseja apostar? "))
            if fichas_apostadas > lista_fichas_jogadores[i]:
                print(f'Jogador {numero_jogadores[i]}, você apostou mais fichas do que estão disponiveis!')
            else:
                lista_fichas_apostadas.append(fichas_apostadas)
                break
    
    #Sorteando as cartas do jogador e banco
    carta1_jogador, valor1_jogador = sorteia_carta(quantos_baralhos, baralho)
    carta2_jogador, valor2_jogador = sorteia_carta(quantos_baralhos, baralho)
    carta1_banco, valor1_banco = sorteia_carta(quantos_baralhos, baralho)
    carta2_banco, valor2_banco = sorteia_carta(quantos_baralhos, baralho)
    
    #Utilizando a função que devolve a soma das cartas, adcionando ou não a terceira carta
    texto_jogador, soma_jogador, jogador_recebeu, valor3 = confere_terceira_carta_jogador(valor1_jogador, valor2_jogador, carta1_jogador, carta2_jogador, 'jogador', valor1_banco, valor2_banco)
    texto_banco, soma_banco = confere_terceira_carta_banco(valor1_banco, valor2_banco, carta1_banco, carta2_banco, 'banco', jogador_recebeu, valor3)

    print(texto_jogador)
    print(texto_banco)
    
    #Aplicando os ifs e atualizando as fichas dos jogadores depois das apostas
    for i in range(quantos_jogadores):
        if lista_quem_aposta[i] == 'jogador': lista_fichas_jogadores[i] = aposta_jogador(soma_jogador, soma_banco, lista_fichas_jogadores[i], lista_fichas_apostadas[i], quantos_baralhos)
        if lista_quem_aposta[i] == 'banco': lista_fichas_jogadores[i] = aposta_banco(soma_jogador, soma_banco, lista_fichas_jogadores[i], lista_fichas_apostadas[i], quantos_baralhos)
        if lista_quem_aposta[i] == 'empate': lista_fichas_jogadores[i] = aposta_empate(soma_jogador, soma_banco, lista_fichas_jogadores[i], lista_fichas_apostadas[i], quantos_baralhos)
    
    #Atualizando as variaveis globais dos jogadores após o resultado da rodada
    quantos_jogadores, numero_jogadores, lista_fichas_jogadores, string_eliminados = atualiza_fichas(quantos_jogadores, numero_jogadores, lista_fichas_jogadores)

    #Imprimindo as fichas para os jogadores
    for i in range(quantos_jogadores):
        print(f'Jogador {numero_jogadores[i]}, você tem {lista_fichas_jogadores[i]} fichas ao final da rodada!')
    
    #Imprimindo quais jogadores zeraram suas fichas na rodada
    for i in range(len(string_eliminados)):
        print(string_eliminados[i])

    #Códigos que terminam o loop da partida, todos jogadores zerarem ou desistirem de jogar
    if quantos_jogadores == 0:
        print('Todos jogadores zeraram suas fichas')
        break

    continua = input("Quer continuar jogando? (sim/não) ")
    if continua == 'não': break

    #limpa o terminal após a rodada
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")
