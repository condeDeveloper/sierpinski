"""Os numeros do README, presos.

Todos sairam do programa antes de entrar aqui.
"""

from sierpinski.medidas import (
    POTENCIAS,
    buraco_entre_as_duas,
    cheia_pelo_produto,
    e_potencia_de_primo,
    linhas_cheias,
    linhas_de_digitos_maximos,
    primeira_quebra,
    quebras_das_potencias,
    tabela_compostos,
    tabela_primos,
)
from sierpinski.nucleo import nao_divisiveis

COMPOSTOS = {
    4: (89, 4, 3, 2),
    6: (113, 4, 4, 5),
    8: (97, 8, 5, 2),
    9: (86, 9, 4, 2),
    10: (107, 5, 4, 6),
    12: (105, 9, 6, 10),
    14: (108, 8, 4, 9),
    15: (107, 6, 5, 7),
}

# Listas INTEIRAS, nao o recorte que a tela mostrou. A primeira versao deste
# bloco veio de um print com [:10] e perdeu o 74 e o 99 do p=5.
CHEIAS = {
    2: ((0, 1, 3, 7, 15, 31, 63), (1, 3, 7, 15, 31, 63)),
    3: ((0, 1, 2, 5, 8, 17, 26, 53, 80), (2, 8, 26, 80)),
    5: ((0, 1, 2, 3, 4, 9, 14, 19, 24, 49, 74, 99), (4, 24)),
}


def test_a_formula_nao_erra_em_nenhum_primo():
    linhas = tabela_primos()
    assert len(linhas) == 8
    assert all(erros == 0 for _, _, erros in linhas)


def test_quantas_linhas_foram_conferidas_nos_primos():
    total = sum(linhas for _, linhas, _ in tabela_primos())
    assert total == 1288


def test_a_formula_quebra_em_todo_composto():
    linhas = tabela_compostos()
    assert len(linhas) == 8
    for m, erros, primeiro, contado, formula in linhas:
        assert erros > 0, m
        assert (erros, primeiro, contado, formula) == COMPOSTOS[m], m


def test_a_formula_erra_nos_dois_sentidos():
    """Em m=4 ela subestima; em m=6 ela superestima."""
    por_m = {m: (contado, formula) for m, _, _, contado, formula in tabela_compostos()}
    contado4, formula4 = por_m[4]
    contado6, formula6 = por_m[6]
    assert contado4 > formula4
    assert contado6 < formula6


def test_nas_potencias_de_primo_a_quebra_cai_em_n_igual_a_m():
    linhas = quebras_das_potencias()
    assert len(linhas) == len(POTENCIAS) == 6
    for m, p, quebra in linhas:
        assert p is not None, m
        assert quebra == m, (m, quebra)


def test_compostos_de_varios_primos_quebram_antes():
    """6, 10, 12, 14 e 15 nao esperam o n chegar em m."""
    for m in (6, 10, 12, 14, 15):
        assert e_potencia_de_primo(m) is None, m
        assert primeira_quebra(m) < m, m


def test_e_potencia_de_primo():
    assert e_potencia_de_primo(4) == 2
    assert e_potencia_de_primo(27) == 3
    assert e_potencia_de_primo(25) == 5
    assert e_potencia_de_primo(6) is None
    assert e_potencia_de_primo(15) is None


def test_linha_cheia_nao_e_digitos_maximos():
    """O achado: a caracterizacao obvia perde linhas, e perde muitas."""
    for p, (cheias, maximos) in CHEIAS.items():
        assert linhas_cheias(p) == cheias, p
        assert linhas_de_digitos_maximos(p) == maximos, p
        assert set(maximos) < set(cheias), p


def test_o_tamanho_do_buraco():
    """E ele cresce com p: em p=5 a caracterizacao obvia pega 2 de 12."""
    assert buraco_entre_as_duas(2) == 1
    assert buraco_entre_as_duas(3) == 5
    assert buraco_entre_as_duas(5) == 10
    assert len(linhas_cheias(5)) == 12
    assert len(linhas_de_digitos_maximos(5)) == 2


def test_a_caracterizacao_certa_e_o_produto():
    """`produto dos digitos mais um == n+1` acerta todas as linhas cheias."""
    for p in (2, 3, 5, 7):
        for n in range(101):
            assert cheia_pelo_produto(n, p) == (nao_divisiveis(n, p) == n + 1), (p, n)
