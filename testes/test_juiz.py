"""A formula dos digitos: ela nunca constroi uma linha.

O ponto do arquivo e que os dois caminhos nao se tocam. Um soma vizinhos
linha a linha; o outro le os digitos de um numero numa base e multiplica.
"""

from sierpinski.juiz import (
    linha_cheia,
    pela_formula,
    todos_os_digitos_sao_o_maximo,
)
from sierpinski.nucleo import nao_divisiveis


def test_formula_em_casos_a_mao():
    # 4 em base 2 e 100: digitos 0, 0, 1 -> 1 * 1 * 2 = 2.
    assert pela_formula(4, 2) == 2
    # 3 em base 2 e 11: digitos 1, 1 -> 2 * 2 = 4.
    assert pela_formula(3, 2) == 4
    assert pela_formula(0, 2) == 1
    assert pela_formula(0, 7) == 1


def test_formula_nunca_passa_do_tamanho_da_linha():
    """Nao da para ter mais entradas nao divisiveis que entradas."""
    for p in (2, 3, 5, 7):
        for n in range(60):
            assert pela_formula(n, p) <= n + 1, (p, n)


def test_formula_e_sempre_positiva():
    """As pontas da linha valem 1, entao nunca sao divisiveis."""
    for p in (2, 3, 5, 7, 11):
        for n in range(60):
            assert pela_formula(n, p) >= 1


def test_formula_contra_contagem_nos_primos_pequenos():
    for p in (2, 3, 5, 7):
        for n in range(80):
            assert pela_formula(n, p) == nao_divisiveis(n, p), (p, n)


def test_a_formula_erra_num_composto():
    """Sem isto, "acerta nos primos" nao teria contraste nenhum."""
    assert pela_formula(4, 4) != nao_divisiveis(4, 4)
    assert nao_divisiveis(4, 4) == 3
    assert pela_formula(4, 4) == 2


def test_linha_cheia_usa_o_produto_e_nao_os_digitos():
    """As duas afirmacoes sao diferentes, e a bateria nao as confunde."""
    assert linha_cheia(5, 3)
    assert not todos_os_digitos_sao_o_maximo(5, 3)
    assert linha_cheia(0, 2)
    assert not todos_os_digitos_sao_o_maximo(0, 2)


def test_digitos_maximos_implica_linha_cheia():
    """Uma direcao vale; a volta e que nao."""
    for p in (2, 3, 5):
        for n in range(100):
            if todos_os_digitos_sao_o_maximo(n, p):
                assert linha_cheia(n, p), (p, n)
