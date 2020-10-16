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
