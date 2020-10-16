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