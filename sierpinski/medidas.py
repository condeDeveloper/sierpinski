"""As tabelas do README.

Tres perguntas:

1. A formula dos digitos bate com a construcao burra, nos primos?
2. E nos compostos, onde ela quebra, e por quanto?
3. Quais linhas nao tem NENHUMA entrada divisivel?

A terceira guarda a correcao mais util deste projeto: "linha cheia" e
"todos os digitos valem p-1" NAO sao a mesma coisa, embora a segunda pareca a
explicacao obvia da primeira.
"""

from functools import lru_cache

from .juiz import pela_formula, todos_os_digitos_sao_o_maximo
from .nucleo import digitos_na_base, e_primo, nao_divisiveis

PRIMOS_FUNDOS = (2, 3, 5, 7)
PRIMOS_RASOS = (11, 13, 17, 19)
COMPOSTOS = (4, 6, 8, 9, 10, 12, 14, 15)
POTENCIAS = (4, 8, 9, 16, 25, 27)
TETO_FUNDO = 200
TETO_RASO = 120


@lru_cache(maxsize=None)
def erros_da_formula(m, teto):
    """Os n em que a formula discorda da contagem direta."""
    return tuple(n for n in range(teto + 1)
                 if nao_divisiveis(n, m) != pela_formula(n, m))


@lru_cache(maxsize=None)
def tabela_primos():
    """(primo, linhas conferidas, erros) para cada primo testado."""
    linhas = []
    for p in PRIMOS_FUNDOS:
        linhas.append((p, TETO_FUNDO + 1, len(erros_da_formula(p, TETO_FUNDO))))
    for p in PRIMOS_RASOS:
        linhas.append((p, TETO_RASO + 1, len(erros_da_formula(p, TETO_RASO))))
    return tuple(linhas)


@lru_cache(maxsize=None)
def tabela_compostos(teto=TETO_RASO):
    """(composto, erros, primeira quebra, contado, formula)."""
    linhas = []
    for m in COMPOSTOS:
        erros = erros_da_formula(m, teto)
        primeiro = erros[0] if erros else None
        linhas.append((
            m,
            len(erros),
            primeiro,
            nao_divisiveis(primeiro, m) if primeiro is not None else None,
            pela_formula(primeiro, m) if primeiro is not None else None,
        ))
    return tuple(linhas)


def e_potencia_de_primo(m):
    """m = p^k para algum primo p e k >= 1?"""
    for p in range(2, m + 1):
        if not e_primo(p):
            continue
        k = p
        while k < m:
            k *= p
        if k == m:
            return p
    return None


@lru_cache(maxsize=None)
def primeira_quebra(m, teto=260):
    """O menor n em que a formula erra, ou None se nao errar ate o teto."""
    for n in range(teto + 1):
        if nao_divisiveis(n, m) != pela_formula(n, m):
            return n
    return None


@lru_cache(maxsize=None)
def quebras_das_potencias():
    """(potencia, primo, primeira quebra) -- a quebra cai em n = m?"""
    return tuple((m, e_potencia_de_primo(m), primeira_quebra(m))
                 for m in POTENCIAS)


@lru_cache(maxsize=None)
def linhas_cheias(p, teto=100):
    """Os n cuja linha nao tem NENHUMA entrada divisivel por p.

    Contado direto, sem formula.
    """
    return tuple(n for n in range(teto + 1) if nao_divisiveis(n, p) == n + 1)


@lru_cache(maxsize=None)
def linhas_de_digitos_maximos(p, teto=100):
    """Os n cujos digitos na base p valem todos p-1.

    Esta e a caracterizacao que PARECE explicar a linha cheia, e nao explica:
    ela so pega um pedaco. Ficou no projeto exatamente para medir o buraco.
    """
    return tuple(n for n in range(teto + 1) if todos_os_digitos_sao_o_maximo(n, p))


def buraco_entre_as_duas(p, teto=100):
    """Quantas linhas cheias a caracterizacao dos digitos maximos perde."""
    return len(linhas_cheias(p, teto)) - len(linhas_de_digitos_maximos(p, teto))


def cheia_pelo_produto(n, p):
    """A caracterizacao CERTA: o produto dos digitos mais um da n+1."""
    return pela_formula(n, p) == n + 1
