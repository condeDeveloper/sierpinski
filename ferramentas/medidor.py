"""Medidor: as tabelas do README em markdown.

    python ferramentas/medidor.py
"""

import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sierpinski.medidas import (  # noqa: E402
    buraco_entre_as_duas,
    linhas_cheias,
    linhas_de_digitos_maximos,
    quebras_das_potencias,
    tabela_compostos,
    tabela_primos,
)


def main():
    t0 = time.time()

    print('## A formula nos primos')
    print()
    print('| p | linhas conferidas | erros |')
    print('|---|---|---|')
    for p, linhas, erros in tabela_primos():
        print('| %d | %d | %d |' % (p, linhas, erros))

    print()
    print('## E nos compostos')
    print()
    print('| m | erros | primeira quebra | contado | formula |')
    print('|---|---|---|---|---|')
    for m, erros, primeiro, contado, formula in tabela_compostos():
        print('| %d | %d | %d | %d | %d |' % (m, erros, primeiro, contado, formula))

    print()
    print('### Potencias de primo')
    print()
    print('| m | base | primeira quebra |')
    print('|---|---|---|')
    for m, p, quebra in quebras_das_potencias():
        print('| %d | %d | %d |' % (m, p, quebra))

    print()
    print('## Linhas sem entrada divisivel')
    print()
    print('| p | cheias (ate 100) | digitos maximos | perdidas |')
    print('|---|---|---|---|')
    for p in (2, 3, 5):
        print('| %d | %s | %s | %d |' % (
            p,
            ', '.join(map(str, linhas_cheias(p))),
            ', '.join(map(str, linhas_de_digitos_maximos(p))),
            buraco_entre_as_duas(p)))

    print()
    print('medido em %.1f s' % (time.time() - t0))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
