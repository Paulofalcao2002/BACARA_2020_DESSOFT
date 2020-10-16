import random
from baralhos import baralho

#função que faz a soma das cartas
def retorna_valor_soma(a, b, c = 0):
    if a + b + c > 9:
        numero = str(a + b + c)
        return int(numero[1])
    else:
        return (a + b + c)

