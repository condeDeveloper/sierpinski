"""Linha de comando.

    python -m sierpinski           tudo
    python -m sierpinski primos    so a tabela dos primos
    python -m sierpinski cheias    so as linhas sem entrada divisivel
"""

import sys

from .medidas import (
    POTENCIAS,
    buraco_entre_as_duas,
    linhas_cheias,
    linhas_de_digitos_maximos,
    quebras_das_potencias,
    tabela_compostos,
    tabela_primos,
)


def primos():
    print('a formula dos digitos contra a construcao, nos primos')
    total = 0
    for p, linhas, erros in tabela_primos():
        print('   p=%-3d linhas conferidas=%-4d erros=%d' % (p, linhas, erros))
        total += erros
    print('   erros somados: %d' % total)
    print()


def compostos():
    print('e nos compostos, onde a hipotese de primo e ignorada')
    for m, erros, primeiro, contado, formula in tabela_compostos():
        print('   m=%-3d erros=%-4d primeira quebra em n=%-3d (contado %d, formula %d)'
              % (m, erros, primeiro, contado, formula))
    print()
    print('   nas potencias de primo a quebra cai exatamente em n = m:')
    for m, p, quebra in quebras_das_potencias():
        print('      m=%-3d = %d^k   primeira quebra em n=%-3d %s'
              % (m, p, quebra, 'igual a m' if quebra == m else 'DIFERE'))
    print()


def cheias():
    print('linhas sem NENHUMA entrada divisivel')
    for p in (2, 3, 5):
        c = linhas_cheias(p)
        d = linhas_de_digitos_maximos(p)
        print('   p=%d' % p)
        print('      cheias:           %s' % list(c))
        print('      digitos maximos:  %s' % list(d))
        print('      a segunda perde %d linhas' % buraco_entre_as_duas(p))
    print()


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else 'tudo'
    if alvo in ('tudo', 'primos'):
        primos()
    if alvo in ('tudo', 'compostos'):
        compostos()
    if alvo in ('tudo', 'cheias'):
        cheias()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
