import random
from baralhos import baralho

#função que faz a soma das cartas
def retorna_valor_soma(a, b, c = 0):
    if a + b + c > 9:
        numero = str(a + b + c)
        return int(numero[1])
    else:
        return (a + b + c)

#função que confere a necessidade da terceira carta e retorna as strings referentes a soma das mesmas
def confere_terceira_carta(a, b, c, d, e):
    if retorna_valor_soma(a, b) <= 5:
        carta3, valor3 = random.choice(list(baralho.items()))
        soma = retorna_valor_soma(a, b, valor3)
        return f'A soma das cartas do {e} foi de {soma}. ' \
               f'Suas cartas foram {c}, {d} e {carta3}', soma
    else:
        soma = retorna_valor_soma(a, b)
        return f'A soma das cartas do {e} foi de {soma}. ' \
               f'Suas cartas foram {c} e {d}', soma
