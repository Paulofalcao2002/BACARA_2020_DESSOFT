# EP - Design de Software
# Equipe: Lorena Budin e Paulo Falcão
# Data: 18/10/2020

import random
import os

#dicionário contendo o baralho original
baralho = {"A de espadas": 1, "A de copas": 1, "A de paus": 1, "A de ouros": 1,
                  "2 de espadas": 2, "2 de copas": 2, "2 de paus": 2, "2 de ouros": 2,
                  "3 de espadas": 3, "3 de copas": 3, "3 de paus": 3, "3 de ouros": 3,
                  "4 de espadas": 4, "4 de copas": 4, "4 de paus": 4, "4 de ouros": 4,
                  "5 de espadas": 5, "5 de copas": 5, "5 de paus": 5, "5 de ouros": 5,
                  "6 de espadas": 6, "6 de copas": 6, "6 de paus": 6, "6 de ouros": 6,
                  "7 de espadas": 7, "7 de copas": 7, "7 de paus": 7, "7 de ouros": 7,
                  "8 de espadas": 8, "8 de copas": 8, "8 de paus": 8, "8 de ouros": 8,
                  "9 de espadas": 9, "9 de copas": 9, "9 de paus": 9, "9 de ouros": 9,
                  "10 de espadas": 10, "10 de copas": 10, "10 de paus": 10, "10 de ouros": 10,
                  "Rainha de espadas": 0, "Rainha de copas": 0, "Rainha de paus": 0, "Rainha de ouros": 0,
                  "Valete de espadas": 0, "Valete de copas": 0, "Valete de paus": 0, "Valete de ouros": 0,
                  "Rei de espadas": 0, "Rei de copas": 0, "Rei de paus": 0, "Rei de ouros": 0}

#função que ajusta a quantidade de baralhos e sorteia as cartas
def sorteia_carta(n, baralho):
    lista_baralhos = [baralho] * n
    i = random.randint(0, n - 1)
    baralho = lista_baralhos[i]

    carta1_jogador, valor1_jogador = random.choice(list(baralho.items()))
    return carta1_jogador, valor1_jogador

#função que faz a soma das cartas
def retorna_valor_soma(a, b, c = 0):
    if a + b + c > 9:
        numero = str(a + b + c)
        return int(numero[1])
    else:
        return (a + b + c)

#funções que conferem a necessidade da terceira carta do jogador e banco, retornando as strings referentes a soma das mesmas
def confere_terceira_carta_jogador(valor1_jogador, valor2_jogador, carta1_jogador, carta2_jogador, string, valor1_banco, valor2_banco):
    if retorna_valor_soma(valor1_jogador, valor2_jogador) <= 5 and retorna_valor_soma(valor1_banco, valor2_banco) < 8:
        jogador_recebeu = True
        carta3, valor3 = random.choice(list(baralho.items()))
        soma = retorna_valor_soma(valor1_jogador, valor2_jogador, valor3)
        return f'A soma das cartas do {string} foi de {soma}. ' \
               f'Suas cartas foram {carta1_jogador}, {carta2_jogador} e {carta3}', soma, jogador_recebeu, valor3
    else:
        jogador_recebeu = False
        valor3 = 0
        soma = retorna_valor_soma(valor1_jogador, valor2_jogador)
        return f'A soma das cartas do {string} foi de {soma}. ' \
               f'Suas cartas foram {carta1_jogador} e {carta2_jogador}', soma, jogador_recebeu, valor3
      
def confere_terceira_carta_banco(valor1_banco, valor2_banco, carta1_banco, carta2_banco, string, jogador_recebeu, valor3_jogador):
    if retorna_valor_soma(valor1_banco, valor2_banco) <= 5 and not jogador_recebeu:
        carta3, valor3 = random.choice(list(baralho.items()))
        soma = retorna_valor_soma(valor1_banco, valor2_banco, valor3)
        return f'A soma das cartas do {string} foi de {soma}. ' \
               f'Suas cartas foram {carta1_banco}, {carta2_banco} e {carta3}', soma
    
    if retorna_valor_soma(valor1_banco, valor2_banco) <= 5 and jogador_recebeu:
        if retorna_valor_soma(valor1_banco, valor2_banco) <= 2:
            carta3, valor3 = random.choice(list(baralho.items()))
            soma = retorna_valor_soma(valor1_banco, valor2_banco, valor3)
            return f'A soma das cartas do {string} foi de {soma}. ' \
                   f'Suas cartas foram {carta1_banco}, {carta2_banco} e {carta3}', soma
    
    if retorna_valor_soma(valor1_banco, valor2_banco) == 3 and valor3_jogador != 8:
            carta3, valor3 = random.choice(list(baralho.items()))
            soma = retorna_valor_soma(valor1_banco, valor2_banco, valor3)
            return f'A soma das cartas do {string} foi de {soma}. ' \
                   f'Suas cartas foram {carta1_banco}, {carta2_banco} e {carta3}', soma
    
    if retorna_valor_soma(valor1_banco, valor2_banco) == 4 and 1 < valor3_jogador < 8:
            carta3, valor3 = random.choice(list(baralho.items()))
            soma = retorna_valor_soma(valor1_banco, valor2_banco, valor3)
            return f'A soma das cartas do {string} foi de {soma}. ' \
                   f'Suas cartas foram {carta1_banco}, {carta2_banco} e {carta3}', soma
    
    if retorna_valor_soma(valor1_banco, valor2_banco) == 5 and 3 < valor3_jogador < 8:
            carta3, valor3 = random.choice(list(baralho.items()))
            soma = retorna_valor_soma(valor1_banco, valor2_banco, valor3)
            return f'A soma das cartas do {string} foi de {soma}. ' \
                   f'Suas cartas foram {carta1_banco}, {carta2_banco} e {carta3}', soma
    else:
            soma = retorna_valor_soma(valor1_banco, valor2_banco)
            return f'A soma das cartas do {string} foi de {soma}. ' \
                   f'Suas cartas foram {carta1_banco} e {carta2_banco}', soma
else:
     soma = retorna_valor_soma(valor1_banco, valor2_banco)
     return f'A soma das cartas do {string} foi de {soma}. ' \
            f'Suas cartas foram {carta1_banco} e {carta2_banco}', soma
          
#função que retorna os valores das comissões de acordo com o número de baralhos
def retona_comissao(quantos_baralhos):
    if quantos_baralhos == 1:
        comissao_jogador = 0.0129
        comissao_banco = 0.0101
        comissao_empate = 0.1575
        return comissao_jogador, comissao_banco, comissao_empate

    if quantos_baralhos == 6:
        comissao_jogador = 0.0124
        comissao_banco = 0.0106
        comissao_empate = 0.1444
        return comissao_jogador, comissao_banco, comissao_empate
      
    if quantos_baralhos == 8:
        comissao_jogador = 0.0124
        comissao_banco = 0.0106
        comissao_empate = 0.1436
        return comissao_jogador, comissao_banco, comissao_empate

#funções que atualizam o número das fichas de acordo com cada tipo de aposta
def aposta_jogador(soma_jogador, soma_banco, fichas, fichas_apostadas, quantos_baralhos):
    if soma_jogador > soma_banco:
        fichas += fichas_apostadas - (retona_comissao(quantos_baralhos)[0] * fichas_apostadas)
        return int(fichas)
    else:
        fichas -= fichas_apostadas
        return fichas

def aposta_banco(soma_jogador, soma_banco, fichas, fichas_apostadas, quantos_baralhos):
    if soma_banco > soma_jogador:
        fichas += (0.95 * fichas_apostadas) - (retona_comissao(quantos_baralhos)[1] * fichas_apostadas)
        return int(fichas)
    else:
        fichas -= fichas_apostadas
        return fichas

def aposta_empate(soma_jogador, soma_banco, fichas, fichas_apostadas, quantos_baralhos):
    if soma_jogador == soma_banco:
        fichas += (8 * fichas_apostadas) - (retona_comissao(quantos_baralhos)[2] * fichas_apostadas)
        return int(fichas)
    else:
        fichas -= fichas_apostadas
        return fichas

#função que atualiza as variaveis globais após a rodada
def atualiza_fichas(jogadores, numero_jogadores, lista_fichas):
    i = 0
    lista_fichas_nova = []
    numero_jogadores_novo = []
    string_eliminados = []
    while i < len(lista_fichas):
        if lista_fichas[i] < 1:
            jogadores -= 1
            string_eliminados.append(f'Jogador {numero_jogadores[i]}, suas fichas acabaram!')
        else:
            lista_fichas_nova.append(lista_fichas[i])
            numero_jogadores_novo.append(numero_jogadores[i])
        i += 1
    return jogadores, numero_jogadores_novo, lista_fichas_nova, string_eliminados
  
print("********")
print("Bem vindo ao Bacará!")
print("********")

fichas = 100

print(f'Todos jogadores começam o jogo com {fichas} fichas. Boa sorte!')

#variaveis que guardam o número de baralhos e jogadores na partida
quantos_baralhos = int(input("Você quer jogar com quantos baralhos? (1/6/8) "))
quantos_jogadores = int(input("Quantos jogadores vão participar? "))

