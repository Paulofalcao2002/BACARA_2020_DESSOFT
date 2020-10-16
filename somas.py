import random
from baralhos import baralho

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
        carta3, valor3 = random.choice(list(baralho.items()))
        soma = retorna_valor_soma(valor1_jogador, valor2_jogador, valor3)
        return f'A soma das cartas do {string} foi de {soma}. ' \
               f'Suas cartas foram {carta1_jogador}, {carta2_jogador} e {carta3}', soma
     else:
        soma = retorna_valor_soma(valor1_jogador, valor2_jogador)
        return f'A soma das cartas do {string} foi de {soma}. ' \
               f'Suas cartas foram {carta1_jogador} e {carta2_jogador}', soma

def confere_terceira_carta_banco(valor1_banco, valor2_banco, carta1_banco, carta2_banco, string):
    if retorna_valor_soma(valor1_banco, valor2_banco) <= 5:
        carta3, valor3 = random.choice(list(baralho.items()))
        soma = retorna_valor_soma(valor1_banco, valor2_banco, valor3)
        return f'A soma das cartas do {string} foi de {soma}. ' \
               f'Suas cartas foram {carta1_banco}, {carta2_banco} e {carta3}', soma
